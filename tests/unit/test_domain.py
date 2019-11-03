def test_new_zipcode_fee(new_zipcode_fee):
    assert isinstance(new_zipcode_fee.region.state, str)
    start = new_zipcode_fee.region.start_zipcode
    end = new_zipcode_fee.region.end_zipcode
    assert (start < end)
