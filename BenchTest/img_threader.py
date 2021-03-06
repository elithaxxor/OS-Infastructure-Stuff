import time
import requsts 
import concurrent.futures 

## Add URL List Here ## 

def randomNum_gen():
    start = .1   # inclusive
    end = .8    # exclusive
    n = 8    # size -- coorleate to 8 max cores, could double tthe time if 4 cores. 
    rand_int = random.uniform(range(start, end), k=n)
    rand_float = rand_int/10
    print(rand_float)

    return rand_float
img_urls = [
 'https://unsplash.com/photos/LVWfjwm_duM'
 'https://unsplash.com/photos/6uneKLGrJPs'
 'https://unsplash.com/photos/YEjrviRMjnA'
 'https://unsplash.com/photos/zilEGfZxwcI'
 'https://unsplash.com/photos/zilEGfZxwcI'
]
## r.text for utf-8 && .content for byte data 
time_now = time.time()
time_c = time.ctime(time_now) 

print(f'start time: {time_c}')
def download_image(img_url): 
    for img_url in img_urls: 
        req = requests.get(img_url)
        req_stat = req.status_code:
        if req_stat == 200 
            img_bytes = requests.get(img_url).content 
            img_name = img_url.split('/')[3] + f{'.jpg}'                                 
            with open(img_name, 'wb') as f:
                f.write(img_bytes) 
        end_time = time.time() 
        end_c = time.ctime(end_time) 
        end_clock = end_time - time_now 
        print(f'Ended processes in {round(end_clock,2)} at {end_c}')

        else: 
            print(f' ## Bad Status {img_url} \n # Return Code {req_stat} ## invalid \n parsing to next URL ## ')
                                                 
                                                 
with concurrent.futures.ThreadPoolExecutor() as executor: 
    rand_float = randomNum_gen 
    executor.map(download_image, rand_float)
