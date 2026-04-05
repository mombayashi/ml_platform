import { useState } from 'react'
import { getSentiment } from '../api'

export default function SentimentPage() {
  const [reviewId, setReviewId] = useState(1)
  const [text, setText] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    try {
      const res = await getSentiment(reviewId, text)
      setResult(res.data)
    } catch (err) {
      setError(err.response?.data?.detail || 'エラーが発生しました')
    } finally {
      setLoading(false)
    }
  }

  const isPositive = result?.sentiment?.label === 'positive'

  return (
    <div>
      <h1 style={styles.title}>レビュー感情分析</h1>
      <p style={styles.desc}>
        レビュー文を解析し、ポジティブ・ネガティブの感情判定を行います。
      </p>
      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          style={{ ...styles.input, width: '120px' }}
          type="number"
          placeholder="レビューID"
          value={reviewId}
          min={1}
          onChange={(e) => setReviewId(Number(e.target.value))}
          required
        />
        <textarea
          style={styles.textarea}
          placeholder="分析したいレビューテキストを入力..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          required
        />
        <button style={styles.button} type="submit" disabled={loading}>
          {loading ? '分析中...' : '感情分析'}
        </button>
      </form>

      {error && <p style={styles.error}>{error}</p>}

      {result && (
        <div style={{ ...styles.resultCard, borderLeft: `5px solid ${isPositive ? '#27ae60' : '#e74c3c'}` }}>
          <p style={styles.text}>「{result.text}」</p>
          <p style={{ ...styles.label, color: isPositive ? '#27ae60' : '#e74c3c' }}>
            {isPositive ? '😊 ポジティブ' : '😞 ネガティブ'}
          </p>
        </div>
      )}
    </div>
  )
}

const styles = {
  title: { fontSize: '1.6rem', marginBottom: '0.5rem' },
  desc: { color: '#666', marginBottom: '1.5rem' },
  form: { display: 'flex', flexDirection: 'column', gap: '0.8rem', maxWidth: '500px' },
  input: { padding: '0.5rem 0.8rem', border: '1px solid #ccc', borderRadius: '4px', fontSize: '1rem' },
  textarea: {
    padding: '0.5rem 0.8rem', border: '1px solid #ccc', borderRadius: '4px',
    fontSize: '1rem', minHeight: '100px', resize: 'vertical',
  },
  button: {
    padding: '0.5rem 1.2rem', background: '#3498db', color: '#fff',
    border: 'none', borderRadius: '4px', cursor: 'pointer', fontSize: '1rem', width: 'fit-content',
  },
  error: { color: 'red' },
  resultCard: {
    background: '#fff', padding: '1.2rem', borderRadius: '8px',
    boxShadow: '0 1px 4px rgba(0,0,0,0.1)', marginTop: '1.5rem',
  },
  text: { color: '#555', marginBottom: '0.8rem', fontStyle: 'italic' },
  label: { fontSize: '1.4rem', fontWeight: 'bold' },
}
