from aiohttp import web

app = web.Application()

# 创建响应内容
async def index(request):
	return web.Response(text='hello aiohttp')

# 设置路由
def setup_routes(app):
	app.router.add_get('/',index)

setup_routes(app)

web.run_app(app,host='127.0.0.1',port = 8000)