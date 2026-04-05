import { useState } from 'react'
import { getClustering } from '../api'

const CLUSTER_COLORS = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']

const SAMPLE_DATA = {
  data: [[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]],
  item_codes: ['A001', 'A002', 'A003', 'A004', 'A005', 'A006'],
}

export default function ClusteringPage() {
  const [rawData, setRawData] = useState(
    SAMPLE_DATA.data.map((row) => row.join(', ')).join('\n')
  )
  const [rawCodes, setRawCodes] = useState(SAMPLE_DATA.item_codes.join(', '))
  const [nClusters, setNClusters] = useState(2)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError(null)

    const data = rawData
      .trim()
      .split('\n')
      .map((line) => line.split(',').map((v) => parseFloat(v.trim())))

    const item_codes = rawCodes.split(',').map((v) => v.trim()).filter(Boolean)

    if (data.length !== item_codes.length) {
      setError('データ行数と商品コード数が一致しません')
      return
    }

    setLoading(true)
    try {
      const res = await getClustering(data, item_codes, nClusters)
      setResult(res.data)
    } catch (err) {
      setError(err.response?.data?.detail || 'エラーが発生しました')
    } finally {
      setLoading(false)
    }
  }

  const grouped = result
    ? result.clusters.reduce((acc, cluster, i) => {
        acc[cluster] = acc[cluster] || []
        acc[cluster].push(result.item_codes[i])
        return acc
      }, {})
    : null

  return (
    <div>
      <h1 style={styles.title}>商品クラスタリング</h1>
      <p style={styles.desc}>
        商品の特徴量（数値）を入力し、K-Meansで商品グループに分類します。
      </p>
      <form onSubmit={handleSubmit} style={styles.form}>
        <label style={styles.fieldLabel}>
          特徴量データ（1行=1商品、カンマ区切り）
          <textarea
            style={styles.textarea}
            value={rawData}
            onChange={(e) => setRawData(e.target.value)}
            required
          />
        </label>
        <label style={styles.fieldLabel}>
          商品コード（カンマ区切り）
          <input
            style={styles.input}
            type="text"
            value={rawCodes}
            onChange={(e) => setRawCodes(e.target.value)}
            required
          />
        </label>
        <label style={styles.fieldLabel}>
          クラスタ数
          <input
            style={{ ...styles.input, width: '80px' }}
            type="number"
            min={2}
            max={10}
            value={nClusters}
            onChange={(e) => setNClusters(Number(e.target.value))}
          />
        </label>
        <button style={styles.button} type="submit" disabled={loading}>
          {loading ? 'クラスタリング中...' : '実行'}
        </button>
      </form>

      {error && <p style={styles.error}>{error}</p>}

      {grouped && (
        <div style={styles.resultCard}>
          <h2 style={styles.subtitle}>クラスタリング結果</h2>
          <div style={styles.clusters}>
            {Object.entries(grouped).map(([cluster, codes]) => (
              <div
                key={cluster}
                style={{
                  ...styles.clusterBox,
                  borderTop: `4px solid ${CLUSTER_COLORS[Number(cluster) % CLUSTER_COLORS.length]}`,
                }}
              >
                <p style={styles.clusterLabel}>クラスタ {cluster}</p>
                <div style={styles.tagGroup}>
                  {codes.map((code) => (
                    <span key={code} style={styles.tag}>{code}</span>
                  ))}
                </div>
              </div>
            ))}
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
  textarea: {
    padding: '0.5rem 0.8rem', border: '1px solid #ccc',
    borderRadius: '4px', fontSize: '1rem', minHeight: '120px', resize: 'vertical',
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
  clusters: { display: 'flex', flexWrap: 'wrap', gap: '1rem' },
  clusterBox: {
    background: '#f8f9fa', padding: '1rem', borderRadius: '6px',
    minWidth: '160px', flex: '1',
  },
  clusterLabel: { fontWeight: 'bold', marginBottom: '0.6rem', color: '#555' },
  tagGroup: { display: 'flex', flexWrap: 'wrap', gap: '0.4rem' },
  tag: {
    background: '#eaf0fb', color: '#2c3e50', padding: '0.25rem 0.5rem',
    borderRadius: '4px', fontSize: '0.85rem',
  },
}
