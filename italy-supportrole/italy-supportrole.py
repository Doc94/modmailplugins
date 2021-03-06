import discord
from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

class SupportRoleManagent(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @group(name="supportrole", invoke_without_command=True)
    @commands.has_any_role(659513332218331155, 676408167063879715)
    async def supportrole(self, ctx: Context) -> None:
        await ctx.send_help(ctx.command)

    @supportrole.command(name="give")
    @commands.has_any_role(659513332218331155, 676408167063879715)
    async def givesupport(self, ctx: Context, user: discord.Member):
        role = get(user.guild.roles, id=683333884871573534)
        if role in user.roles:
            await ctx.send(f"Hey **{ctx.author.name}**, il ruolo <@&{role.id}> è già stato assegnato a **{user.name}**.")
        else:
            await user.add_roles(role)
            await ctx.send(f"Hey **{ctx.author.name}**, il ruolo <@&{role.id}> è stato assegnato correttamente a **{user.name}**.")

    @supportrole.command(name="remove")
    @commands.has_any_role(659513332218331155, 676408167063879715)
    async def removesupport(self, ctx: Context, user: discord.Member):
        role = get(user.guild.roles, id=683333884871573534)
        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(f"Hey **{ctx.author.name}**, il ruolo <@&{role.id}> è stato rimosso correttamente a **{user.name}**.")
        else:
            await ctx.send(f"Hey **{ctx.author.name}**, il ruolo <@&{role.id}> non è ancora stato assegnato a **{user.name}**.")

def setup(bot):
    bot.add_cog(SupportRoleManagent(bot))
