import { useState } from 'react'
import { getTimeseries } from '../api'

export default function TimeseriesPage() {
  const [inputData, setInputData] = useState('100, 102, 105, 103, 108, 110')
  const [periods, setPeriods] = useState(5)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError(null)
    const data = inputData.split(',').map((v) => parseFloat(v.trim())).filter((v) => !isNaN(v))
    if (data.length < 3) {
      setError('データは3点以上入力してください')
      return
    }
    setLoading(true)
    try {
      const res = await getTimeseries(data, periods)
      setResult(res.data)
    } catch (err) {
      setError(err.response?.data?.detail || 'エラーが発生しました')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <h1 style={styles.title}>時系列予測</h1>
      <p style={styles.desc}>
        過去の数値データを入力し、ホルト・ウィンタース法で将来を予測します。
      </p>
      <form onSubmit={handleSubmit} style={styles.form}>
        <label style={styles.fieldLabel}>
          過去データ（カンマ区切り）
          <input
            style={styles.input}
            type="text"
            value={inputData}
            onChange={(e) => setInputData(e.target.value)}
            required
          />
        </label>
        <label style={styles.fieldLabel}>
          予測期間（ステップ数）
          <input
            style={{ ...styles.input, width: '100px' }}
            type="number"
            min={1}
            max={30}
            value={periods}
            onChange={(e) => setPeriods(Number(e.target.value))}
          />
        </label>
        <button style={styles.button} type="submit" disabled={loading}>
          {loading ? '予測中...' : '予測実行'}
        </button>
      </form>

      {error && <p style={styles.error}>{error}</p>}

      {result && (
        <div style={styles.resultCard}>
          <h2 style={styles.subtitle}>予測結果（{result.forecast.length}ステップ）</h2>
          <div style={styles.dataRow}>
            <div>
              <p style={styles.sectionLabel}>入力データ</p>
              <div style={styles.tagGroup}>
                {result.input_data.map((v, i) => (
                  <span key={i} style={styles.tag}>{v.toFixed(1)}</span>
                ))}
              </div>
            </div>
            <div>
              <p style={styles.sectionLabel}>予測値</p>
              <div style={styles.tagGroup}>
                {result.forecast.map((v, i) => (
                  <span key={i} style={{ ...styles.tag, background: '#d5f5e3', color: '#1e8449' }}>
                    {v.toFixed(2)}
                  </span>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

const styles = {
  title: { fontSize: '1.6rem', marginBottom: '0.5rem' },
  subtitle: { fontSize: '1.1rem', marginBottom: '1rem' },
  desc: { color: '#666', marginBottom: '1.5rem' },
  form: { display: 'flex', flexDirection: 'column', gap: '0.8rem', maxWidth: '500px' },
  fieldLabel: { display: 'flex', flexDirection: 'column', gap: '0.3rem', fontWeight: 'bold' },
  input: {
    padding: '0.5rem 0.8rem', border: '1px solid #ccc',
    borderRadius: '4px', fontSize: '1rem', width: '100%',
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
  dataRow: { display: 'flex', flexDirection: 'column', gap: '1rem' },
  sectionLabel: { fontWeight: 'bold', marginBottom: '0.4rem', color: '#555' },
  tagGroup: { display: 'flex', flexWrap: 'wrap', gap: '0.4rem' },
  tag: {
    background: '#eaf0fb', color: '#2c3e50', padding: '0.3rem 0.6rem',
    borderRadius: '4px', fontSize: '0.9rem',
  },
}
