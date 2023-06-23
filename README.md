## Introduction

**db-storage1111 is an extension for [AUTOMATIC1111's Stable Diffusion Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui).**

It allows to store pictures to databases.At the moment it only supports MongoDB.
## Features

- **Store images on a MongoDB instance**

## Installation

1. Visit the **Extensions** tab of Automatic's WebUI.
2. Visit the **Install from URL** subtab.
3. Paste this repo's URL into the first field: `https://github.com/takoyaro/db-storage1111
4. Click **Install**.


## Usage
Set environment variables if needed before starting the app:
| Variable | Default       |
|----------|---------------|
| `DB_HOST`  | `'localhost'` |
| `DB_PORT`  | `27017`       |
| `DB_USER`  | `""`          |
| `DB_PASS`  | `""`          |

Then, simply check the `Save to DB` checkbox and generate!


## Contributing
I barely write any python, I have no doubt this extension could be improved and optimized. Feel free to submit PRs!


```sql
CREATE TABLE `generated_images` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `prompt` text COMMENT '图片生成的 prompt',
  `negative_prompt` text COMMENT '图片生成的 negative_prompt',
  `steps` varchar(255) DEFAULT NULL COMMENT '图片生成的 steps',
  `seed` varchar(255) DEFAULT NULL COMMENT '图片生成的 seed',
  `sampler` varchar(255) DEFAULT NULL COMMENT '图片生成的 sampler',
  `cfg_scale` varchar(255) DEFAULT NULL COMMENT '图片生成的 cfg_scale',
  `size` varchar(255) DEFAULT NULL COMMENT '图片生成的 size，例如 512x512',
  `model_hash` varchar(255) DEFAULT NULL COMMENT '图片生成的 model 的 hash 值',
  `model` varchar(255) DEFAULT NULL COMMENT '图片生成的 model',
  `image_base64` mediumtext COMMENT '图片数据，base64格式',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```