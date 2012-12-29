def assert_raises(call, exception):
    throwsException = False
    try:
        call()
    except exception:
        throwsException = True
    
    assert throwsException