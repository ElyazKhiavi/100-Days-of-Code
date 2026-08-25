

def calculate(**kwargs):
    return type(kwargs) # dict


print(calculate())



class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color', 'black')
        self.seats = kw.get('seats', 4)
    def __str__(self):
        return f'Car:{self.make.title()} {self.model.title()} Seats: {self.seats} Color:{self.color}'

my_car = Car(make='benz',model='C-Class')
print(my_car)
# Examples


###  Building a user profile with optional fields
def build_profile(first, last, **user_info):
    """Create a dictionary with required and optional user details."""
    profile = {"first_name": first, "last_name": last}
    profile.update(user_info)
    return profile

# Call with any extra info you want
user1 = build_profile("Alice", "Smith", age=30, city="London", job="Developer")
user2 = build_profile("Bob", "Jones", hobby="guitar", pet="dog")

print(user1)
print(user2)


### Configuration / settings for a game or app

def start_game(**settings):
    """Start a game with optional settings. Provide defaults if not given."""
    defaults = {
        "difficulty": "normal",
        "sound": True,
        "volume": 50,
        "fullscreen": False
    }
    defaults.update(settings)   # override defaults with user choices
    print("Game starting with:", defaults)

start_game()                      # all defaults
start_game(difficulty="hard", fullscreen=True)
start_game(volume=0, sound=False)



### Passing options to a formatting function

def format_text(text, **options):
    """Format text with optional styling flags."""
    if options.get("upper"):
        text = text.upper()
    if options.get("bold"):
        text = f"**{text}**"
    if options.get("prefix"):
        text = f"{options['prefix']} {text}"
    return text

print(format_text("hello", upper=True))
print(format_text("hello", bold=True, prefix=">>"))
print(format_text("hello"))                    # no options




