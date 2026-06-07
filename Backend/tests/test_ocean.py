import sys
import os

project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, project_root)

from services.ocean import OceanClient

ocean = OceanClient()

companies = ocean.get_similar_companies("stripe.com")

print(companies)