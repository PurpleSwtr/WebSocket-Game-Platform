import { apiClient } from "@/api";

export const useApi = {
  get: (endpoint: string) => apiClient.get(endpoint),
  delete: (endpoint: string) => apiClient.delete(endpoint),
  patch: (endpoint: string, payload: any) => apiClient.patch(endpoint, payload),
  post: (endpoint: string, payload: any) => apiClient.post(endpoint, payload),
};

// Использование
// const result = await apiAsync.get('/users');
// const result = await apiAsync.delete('/users/1');
