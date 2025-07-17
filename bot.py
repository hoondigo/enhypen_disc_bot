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


# Shared function to generate a command dynamically
def create_image_command(name, desc):
    @interactions.slash_command(name=name, description=desc)
    async def image_command(ctx: interactions.SlashContext):
        image_path = get_random_image(name)
        if image_path:
            await ctx.send(files=interactions.File(image_path))
        else:
            await ctx.send(f"No {name.capitalize()} images found!")
    return image_command


# Register all image commands
create_image_command("jungwon", "Get a random image of Jungwon")
create_image_command("heeseung", "Get a random image of Heeseung")
create_image_command("jay", "Get a random image of Jay")
create_image_command("jake", "Get a random image of Jake")
create_image_command("sunghoon", "Get a random image of Sunghoon")
create_image_command("sunoo", "Get a random image of Sunoo")
create_image_command("ni_ki", "Get a random image of Ni-ki")

# Keep alive (only needed if running on Render with web service)
keep_alive()

# Start the bot
bot.start()
