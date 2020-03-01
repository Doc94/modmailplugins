import discord
from discord.ext import commands

class SupportRoleManagent(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @bot.command(pass_context=True)
    @commands.has_any_role(659513332218331155, 676408167063879715)
    async def givesupport(ctx, user: discord.Member):
        role = get(guild.roles, id=683333884871573534)
        await user.add_roles(role)
        await await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")

    @bot.command(pass_context=True)
    @commands.has_any_role(659513332218331155, 676408167063879715)
    async def removesupport(ctx, user: discord.Member):
        role = get(guild.roles, id=683333884871573534)
        await user.remove_roles(role)
        await await ctx.send(f"hey {ctx.author.name}, {user.name} has been remove of a role called: {role.name}")


def setup(bot):
    bot.add_cog(SupportRoleManagent(bot))