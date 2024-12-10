import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/weerobot/api';

// axios 인스턴스 생성
const axiosInstance = axios.create({
  baseURL: BASE_URL,
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  }
});

// 요청 인터셉터
axiosInstance.interceptors.request.use(
  (config) => {
    console.log('API Request:', config.url);
    return config;
  },
  (error) => {
    console.error('Request Error:', error);
    return Promise.reject(error);
  }
);

// 응답 인터셉터
axiosInstance.interceptors.response.use(
  (response) => {
    console.log('API Response:', response.data);
    return response;
  },
  (error) => {
    console.error('Response Error:', error);
    return Promise.reject(error);
  }
);

export const apiClient = {
  getRobots: () => axiosInstance.get('/robot/'),
  getCCTVs: () => axiosInstance.get('/cctv/'),
  getCCTVLogs: () => axiosInstance.get('/cctv/log/'),
  getRobotLogs: () => axiosInstance.get('/robot/log/'),
  getChatLogs: () => axiosInstance.get(`/robot/log/chat/`),
};