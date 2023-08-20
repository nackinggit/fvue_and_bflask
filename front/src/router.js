//从下载的vue-router中导入createRouter
import { createRouter, createWebHistory, createWebHashHistory } from "vue-router"
import Login from "./components/Login.vue"
import Chat from "./components/Chat.vue"
//配置映射关系
const routes = [
    //默认
    {
        path: '/',
        //重定向
        redirect: "/chat"
    },
    {
        path: "/login",
        component: Login
    },
    {
        path: "/chat",
        component: Chat
    }
]

//创建路由对象
const router = createRouter({
    routes,
    history: createWebHistory()
})

router.beforeEach((to, from, next) => {
    if (to.path == '/login') {
        // 登录或者注册才可以往下进行
        next();
    } else {
        // 获取 token
        const token = localStorage.getItem('uname');
        console.log(token)
        // token 不存在
        if (token === null || token === '') {
            alert('您还没有登录，请先登录');
            next('/login');
        } else {
            next();
        }
    }
})

export default router