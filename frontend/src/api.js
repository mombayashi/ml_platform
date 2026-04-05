import axios from 'axios'

const api = axios.create({ baseURL: '/api' })

export const getRecommendations = (keyword, top_n = 5) =>
  api.post('/recommendation/', { keyword, top_n })

export const getSentiment = (review_id, text) =>
  api.post('/sentiment/', { review_id, text })

export const getTimeseries = (data, periods) =>
  api.post('/timeseries/', { data, periods })

export const getClustering = (data, item_codes, n_clusters) =>
  api.post('/clustering/', { data, item_codes, n_clusters })
