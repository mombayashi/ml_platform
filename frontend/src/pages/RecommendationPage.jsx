import { useState } from 'react'
import { getRecommendations } from '../api'

export default function RecommendationPage() {
  const [keyword, setKeyword] = useState('')
  const [topN, setTopN] = useState(5)
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    try {
      const res = await getRecommendations(keyword, topN)
      setResults(res.data)
    } catch (err) {
      setError(err.response?.data?.detail || 'エラーが発生しました')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <h1 style={styles.title}>類似商品推薦</h1>
      <p style={styles.desc}>
        楽天の商品データをTF-IDFでベクトル化し、コサイン類似度で類似商品を推薦します。
      </p>
      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          style={styles.input}
          type="text"
          placeholder="キーワード（例: ワイヤレスイヤホン）"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          required
        />
        <label style={styles.label}>
          件数:
          <input
            style={{ ...styles.input, width: '80px', marginLeft: '0.5rem' }}
            type="number"
            min={1}
            max={20}
            value={topN}
            onChange={(e) => setTopN(Number(e.target.value))}
          />
        </label>
        <button style={styles.button} type="submit" disabled={loading}>
          {loading ? '検索中...' : '推薦を取得'}
        </button>
      </form>

      {error && <p style={styles.error}>{error}</p>}

      {results && (
        <div>
          <h2 style={styles.subtitle}>「{results.keyword}」の推薦結果</h2>
          {results.results.length === 0 ? (
            <p>結果が見つかりませんでした。</p>
          ) : (
            <ul style={styles.list}>
              {results.results.map((item, i) => (
                <li key={i} style={styles.card}>
                  <a href={item.url} target="_blank" rel="noreferrer" style={styles.itemName}>
                    {item.name}
                  </a>
                  <div style={styles.meta}>
                    <span>¥{item.price?.toLocaleString()}</span>
                    <span>{item.shop}</span>
                    <span style={styles.score}>
                      類似度: {(item.similarity_score * 100).toFixed(1)}%
                    </span>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  )
}

const styles = {
  title: { fontSize: '1.6rem', marginBottom: '0.5rem' },
  subtitle: { fontSize: '1.2rem', margin: '1.5rem 0 0.8rem' },
  desc: { color: '#666', marginBottom: '1.5rem' },
  form: { display: 'flex', gap: '0.8rem', flexWrap: 'wrap', alignItems: 'center', marginBottom: '1rem' },
  input: { padding: '0.5rem 0.8rem', border: '1px solid #ccc', borderRadius: '4px', fontSize: '1rem' },
  label: { display: 'flex', alignItems: 'center', fontSize: '1rem' },
  button: {
    padding: '0.5rem 1.2rem', background: '#3498db', color: '#fff',
    border: 'none', borderRadius: '4px', cursor: 'pointer', fontSize: '1rem',
  },
  error: { color: 'red', margin: '0.5rem 0' },
  list: { listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.8rem' },
  card: {
    background: '#fff', padding: '1rem', borderRadius: '8px',
    boxShadow: '0 1px 4px rgba(0,0,0,0.1)',
  },
  itemName: { fontWeight: 'bold', color: '#2c3e50', textDecoration: 'none', fontSize: '1rem' },
  meta: { display: 'flex', gap: '1rem', marginTop: '0.4rem', color: '#666', fontSize: '0.9rem' },
  score: { color: '#27ae60', fontWeight: 'bold' },
}
