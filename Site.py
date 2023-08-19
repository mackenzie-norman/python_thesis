import matplotlib.transforms as transforms
from svgpath2mpl import parse_path
from svgpathtools import svg2paths
class Site:
    def __init__(self, name, lat, long):
        self.name = name
        self.lat = lat
        self.long = long
        self.sightings = []

    def add_sighting(self, sighting):
        self.sightings.append(sighting)
    
    def get_sightings(self):
        return self.sightings
    def __len__(self):
        return len(self.sightings)
    def get_name(self):
        return self.name

    def get_latitude(self):
        return self.lat

    def get_longitude(self):
        return self.long
    def get_sightings_by_animal(self):
        animal_dict = {}
        for a in self.sightings:
            if(a.name not in animal_dict.keys()):
                print(animal_dict.keys())
                animal_dict[a.name] = []
            animal_dict[a.name].append(a)
        return animal_dict
    def __str__(self):
        return f"Site: {self.name}, Latitude: {self.lat}, Longitude: {self.long}, Sightings: {len(self.sightings)}"
    
class Animal:
    def __init__(self, name):
        self.name = name
        if("squirrel" in name):
            tmp_path, attributes = svg2paths('svgs/squirrel-cute.svg')
        else:
            tmp_path, attributes = svg2paths('svgs/coyote-cute.svg')
        tmp_marker = parse_path(attributes[0]['d'])

        # Apply transformations
        tmp_marker.vertices -= tmp_marker.vertices.mean(axis=0)
        tmp_marker = tmp_marker.transformed(transforms.Affine2D().rotate_deg(180))
        tmp_marker = tmp_marker.transformed(transforms.Affine2D().scale(-1, 1))
        self.marker =  tmp_marker
    def get_animal(self):
        return self.animal
    def get_animal(self):
        return self.name
    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, other) -> bool:
        if(self.name == other.name):
            return True
        return False
class Sighting(Animal):
    def __init__(self, date, animal, site):
        super().__init__(animal)
        self.date = date
        self.site = site

    def get_date(self):
        return self.date


    def get_site(self):
        return self.site

    def __str__(self):
        return f"Date: {self.date}, Animal: {self.name}, Location: {self.site.name}"
    def __eq__(self, other) -> bool:
        return super().__eq__(other)

