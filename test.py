from miio import DeviceFactory

dev = DeviceFactory.create("192.168.1.34", "7579554b42774252735343654c677539")
dev.status()