from TV import TV

def TestTV():
    tv1 = TV()
    tv1.turnOn()
    
    tv1_channel = int(input("Enter the channel for tv1 (1-120): "))
    tv1_volume = int(input("Enter the volume level for tv1 (1-7): "))
    tv1.setChannel(tv1_channel)
    tv1.setVolume(tv1_volume)
    
    tv2 = TV()
    tv2.turnOn()
    
    
    tv2_channel = int(input("Enter the channel for tv2 (1-120): "))
    tv2_volume = int(input("Enter the volume level for tv2 (1-7): "))
    tv2.setChannel(tv2_channel)
    tv2.setVolume(tv2_volume)

    print(f"tv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}")
    print(f"tv2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}")

TestTV()