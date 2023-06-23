import base64
from io import BytesIO
import os
import re
import modules.scripts as scripts
import gradio as gr

from scripts.lib.mysql import Mysql

db_host = os.environ.get('DB_HOST', 'localhost')
db_port = int(os.environ.get('DB_PORT', 3306))
db_user = os.environ.get('DB_USER', 'root')
db_password = os.environ.get('DB_PASS', 'anywhere')
db_database = os.environ.get('DB_PASS', 'ai_project')

class Scripts(scripts.Script):
    def title(self):
        return "Mysql Storage"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        checkbox_save_to_db = gr.inputs.Checkbox(label="Save to DB", default=False)
        table_name = gr.inputs.Textbox(label="Collection Name", default="Automatic1111")
        return [checkbox_save_to_db, table_name]

    def postprocess(self, p, processed, checkbox_save_to_db, table_name):
        sql = Mysql(db_host, db_port, db_user, db_password, db_database) if checkbox_save_to_db else None
        if sql is None:
            return True
    
        print("test hykes")
        for i in range(len(processed.images)):

            # Extract image information
            regex = r"Steps:.*$"
            seed = processed.seed
            prompt = processed.prompt
            neg_prompt = processed.negative_prompt
            info = re.findall(regex, processed.info, re.M)[0]
            input_dict = dict(item.split(": ") for item in str(info).split(", "))
            print(input_dict)
            
            steps = int(input_dict["Steps"])
            seed = int(input_dict["Seed"])
            sampler = input_dict["Sampler"]
            cfg_scale = float(input_dict["CFG scale"])
            size = tuple(map(int, input_dict["Size"].split("x")))
            model_hash = input_dict["Model hash"]
            model = input_dict["Model"]

            image = processed.images[i]
            buffer = BytesIO()
            image.save(buffer, "png")
            image_bytes = buffer.getvalue()

            sql.inset_db(table_name, {
                "prompt": prompt, 
                "negative_prompt": neg_prompt, 
                "steps": int(steps), 
                "seed": int(seed), 
                "sampler": sampler,
                "cfg_scale": float(cfg_scale), 
                "size": size, 
                "model_hash": model_hash, 
                "model": model, 
                "image": image_bytes
            })
        return True
