from fastapi import FastAPI,Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from typing import Dict
import uvicorn
app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:63342",
    "https://flames-game-api.onrender.com"

]

app.add_middleware(CORSMiddleware, allow_origins =origins, allow_methods = ["*"])
@app.post("/check")
async def check(names:Dict = Body(...)):
    names = jsonable_encoder(names)
    # name1 = lst[0]
    # name2 = lst[1]
    name1 = names['name1']
    name2 = names['name2']


    try:
        def name_2_dict(name):
            out = {}
            for n1 in name:
                if n1 in out:
                    out[n1] += 1
                else:
                    out[n1] = 1
            return out

        name1_dict = name_2_dict(name1)
        name2_dict = name_2_dict(name2)

        final = {}
        for k, v in name1_dict.items():
            if k not in name2_dict:
                final[k] = v
            else:
                if name1_dict[k] == name2_dict[k]:
                    pass
                else:
                    final[k] = name1_dict[k] - name2_dict[k]

        for k, v in name2_dict.items():
            if k not in name1_dict:
                final[k] = v
            else:
                if name1_dict[k] == name2_dict[k]:
                    pass
                else:
                    final[k] = name1_dict[k] - name2_dict[k]

        diff = sum([*final.values()])

        def rem(no, div):
          if no < div + 1 and no % div == 0:
            return no
          else:
              while no > div:
                  no = no % div
              if no == 0:
                  return div
              else:
                  return no

        out = ['f', 'l', 'a', 'm', 'e', 's']

        flames = {
        'f': "Friend",
        'l': "Love",
        'a': "Anbu",
        'm': 'Marriage',
        'e': 'Enemy',
        's': 'Sisters'
         }

        for i in [6, 5, 4, 3, 2]:
             out.pop(rem(diff, i) - 1)

        return flames[out[0]]

    except Exception as e:
        return e
