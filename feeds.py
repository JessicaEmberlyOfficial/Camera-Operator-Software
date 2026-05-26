import os
def feeds():
  os.system("clear")
  
  # a1 – 565 W 5th Ave, Colville, WA 99114
  # b1 – 308 2nd St SW, Jamestown, ND 58401
  # b2 – 804 Main Ave, Oakes, ND 58474
  # c1 – 8, South 18th Avenue West, Duluth, MN 55806
  # d1 – 555 Main St, Meeker, CO 81641
  # e1 – 1125 Grandview St, Page, AZ 86040
  # f1 – 2007 US-77, Kingsville, TX 78363
  # g1 – Unknown, Hicksville, NY,11801
  # h1 – 315 OH-177, Hamilton, OH 45011

  question = input("""
Businesses (Washington)
(a1). Business – Vaagen Brothers Lumber Inc (Colville, WA) – 68.116.13.142

Businesses (North Dakota)
(b1). Business – CSI Cable Internet (Jamestown, ND) – 64.77.205.140
(b2). Business – Oakes High School (Oakes, ND) – 165.234.182.103

Businesses (Minnesota)
(c1). Business – Aerostich (Duluth, MN) – 24.158.26.12

Businesses (Colorado)
(d1). Business – Rio Blanco County (Meeker, CO) – 68.170.44.165

Businesses (Arizona)
(e1). Business – Westview Residences (Page, AZ) – 198.71.120.207

Businesses (Texas)
(f1). Business – Neessen Chevrolet GMC (Kingsville, TX) – 67.61.139.162

Houses (New York)
(g1). House – Unknown (Hicksville, NY) – 47.23.136.226

Businesses (Ohio)
(h1). Butler County Government Services (Hamilton, Ohio) – https://gsccam.butlersheriff.org/

Which do I open?: """)

  # NORTH RAILROAD S
  if question == "a1":
    os.system("termux-open-url http://68.116.13.142:81/camera/index.html#/video")
  
  # 1ST ST ST W
  if question == "b1":
    os.system("termux-open-url http://64.77.205.140/view/viewer_index.shtml")
    
  # 804 MAIN AVE
  if question == "b2":
    os.system("termux-open-url http://165.234.182.103/mjpg/video.mjpg")
  
  # 8 S 18th AVE W
  if question == "c1":
    os.system("termux-open-url http://24.158.26.12:8888/mjpg/video.mjpg")
 
 # 555 MAIN ST
  if question == "d1":
    os.system("termux-open-url http://68.170.44.165/mjpg/video.mjpg")
    
  # 1125 GRANDVIEW ST
  if question == "e1":
    os.system("termux-open-url http://198.71.120.207:8080/")
  
  # 2007 US-77
  if question == "f1":
    os.system("termux-open-url http://67.61.139.162:8080/")
  
  # UNKNOWN
  if question == "g1":
    os.system("termux-open-url http://47.23.136.226:1024/sv/sv.html#home")

  # 315 OH-177
  if question == "h1":
    os.system("termux-open-url https://gsccam.butlersheriff.org/camera/index.html#/video")