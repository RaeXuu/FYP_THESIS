
  方案 A（推荐，开发期间）：关掉 overlayroot
  overlayroot=tmpfs console=tty1 root=PARTUUID=...
        
  这是 /boot/firmware/cmdline.txt，需要改那里：                                                                    
    
  sudo mount -o remount,rw /boot/firmware                                                                          
  sudo nano /boot/firmware/cmdline.txt
                                                    
  找到 overlayroot=tmpfs，把这一段删掉（只删这个词，其他参数保持在同一行），然后：                                 
                                        
  sudo mount -o remount,ro /boot/firmware                                                                          
  sudo reboot          