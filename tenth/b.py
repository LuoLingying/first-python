def outside():
    var = 5
    def inside():
        print(var)
        var = 3   
        
    inside()
outside()
