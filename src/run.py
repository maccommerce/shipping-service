# import app and run server
from app.resources.repository.region_fee import RegionFee

my_repo = RegionFee()
fee = my_repo.findByZipcode(7000)
print(fee.region.state)