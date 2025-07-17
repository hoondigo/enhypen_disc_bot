import interactions
import os
import random
from keep_alive import keep_alive

# Load the bot using token from environment variables
bot = interactions.Client(token=os.getenv("DISCORD_TOKEN"))

# Utility function to get a random image from a folder
def get_random_image(category):
    folder = os.path.join("images", category)
    if not os.path.exists(folder):
        return None
    images = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    if not images:
        return None
    return os.path.join(folder, random.choice(images))


# Individual slash commands

@interactions.slash_command(name="jungwon", description="Get a random image of Jungwon")
async def jungwon(ctx):
    image_path = get_random_image("jungwon")
    if image_path:
        await ctx.send(files=interactions.File(image_path))
    else:
        await ctx.send("No Jungwon images found!")

@interactions.slash_command(name="heeseung", description="Get a random image of Heeseung")
async def heeseung(ctx):
    image_path = get_random_image("heeseung")
    if image_path:
        await ctx.send(files=interactions.File(image_path))
    else:
        await ctx.send("No Heeseung images found!")

@interactions.slash_command(name="jay", description="Get a random image of Jay")
async def jay(ctx):
    image_path = get_random_image("jay")
    if image_path:
        await ctx.send(files=interactions.File(image_path))
    else:
        await ctx.send("No Jay images found!")

@interactions.slash_command(name="jake", description="Get a random image of Jake")
async def jake(ctx):
    image_path = get_random_image("jake")
    if image_path:
        await ctx.send(files=interactions.File(image_path))
    else:
        await ctx.send("No Jake images found!")

@interactions.slash_command(name="sunghoon", description="Get a random image of Sunghoon")
async def sunghoon(ctx):
    image_path = get_random_image("sunghoon")
    if image_path:
        await ctx.send(files=interactions.File(image_path))
    else:
        await ctx.send("No Sunghoon images found!")

@interactions.slash_command(name="sunoo", description="Get a random image of Sunoo")
async def sunoo(ctx):
    image_path = get_random_image("sunoo")
    if image_path:
        await ctx.send(files=interactions.File(image_path))
    else:
        await ctx.send("No Sunoo images found!")

@interactions.slash_command(name="ni_ki", description="Get a random image of Ni-ki")
async def ni_ki(ctx):
    image_path = get_random_image("ni_ki")
    if image_path:
        await ctx.send(files=interactions.File(image_path))
    else:
        await ctx.send("No Ni-ki images found!")

@interactions.slash_command(name="enhypen", description="Get a random image of the group Enhypen")
async def enhypen(ctx):
    image_path = get_random_image("enhypen")
    if image_path:
        await ctx.send(files=interactions.File(image_path))
    else:
        await ctx.send("No Enhypen group images found!")


# Keep alive (for Render)
keep_alive()

# Start the bot
bot.start()
