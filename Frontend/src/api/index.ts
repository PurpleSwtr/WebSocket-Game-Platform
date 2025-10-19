import { BackendURL } from '@/types/types';
import axios from 'axios';

export const apiClient = axios.create({
  baseURL: `http://${BackendURL}`,
  withCredentials: true
});
