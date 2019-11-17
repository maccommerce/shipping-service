# import app and run server
from app.resources.repository.region_fee import RegionFee
from app import app



if __name__ == "__main__":
    app.run(debug=True)

# my_repo = RegionFee()
# fee = my_repo.findByZipcode(7000)
# print(fee.region.state)