import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/weerobot/api';

export const apiClient = {
  getRobots: () => axios.get(`${BASE_URL}/robot/`),
  getCCTVs: () => axios.get(`${BASE_URL}/cctv/`),
  getCCTVLogs: () => axios.get(`${BASE_URL}/cctv/log/`),
  getRobotLogs: () => axios.get(`${BASE_URL}/robot/log/`),
  getChatLogs: (robotId) => axios.get(`${BASE_URL}/robot/log/chat/${robotId}`),
};