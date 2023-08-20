import axios from 'axios'
import router from './router'

axios.defaults.withCredentials = true;  // 设置cross跨域 并设置访问权限 允许跨域携带cookie信息

// axios.defaults.headers.post['Content-Type'] = 'application/json'
// axios.defaults.headers.put['Content-Type'] = 'application/json'

// http request 拦截器
axios.interceptors.request.use(
  config => {
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// http response 拦截器
axios.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    if (401 == error.response.status) {
      alert("请输入验证码登录")
      localStorage.clear()
      router.replace({
        path: '/login',
        query: { redirect: router.currentRoute.fullPath }
      })
    }
    return Promise.reject(error) // 返回接口返回的错误信息
  }
);

export default function () {
  return axios
}