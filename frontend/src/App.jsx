import { BrowserRouter, Routes, Route, NavLink } from 'react-router-dom'
import RecommendationPage from './pages/RecommendationPage'
import SentimentPage from './pages/SentimentPage'
import TimeseriesPage from './pages/TimeseriesPage'
import ClusteringPage from './pages/ClusteringPage'

const navStyle = {
  display: 'flex',
  gap: '1rem',
  background: '#2c3e50',
  padding: '1rem 2rem',
}

const linkStyle = {
  color: '#ecf0f1',
  textDecoration: 'none',
  fontWeight: 'bold',
  padding: '0.4rem 0.8rem',
  borderRadius: '4px',
}

const activeLinkStyle = {
  ...linkStyle,
  background: '#3498db',
}

export default function App() {
  return (
    <BrowserRouter>
      <nav style={navStyle}>
        <span style={{ color: '#ecf0f1', fontWeight: 'bold', marginRight: '1rem' }}>
          ML Platform
        </span>
        <NavLink
          to="/"
          end
          style={({ isActive }) => isActive ? activeLinkStyle : linkStyle}
        >
          推薦
        </NavLink>
        <NavLink
          to="/sentiment"
          style={({ isActive }) => isActive ? activeLinkStyle : linkStyle}
        >
          感情分析
        </NavLink>
        <NavLink
          to="/timeseries"
          style={({ isActive }) => isActive ? activeLinkStyle : linkStyle}
        >
          時系列予測
        </NavLink>
        <NavLink
          to="/clustering"
          style={({ isActive }) => isActive ? activeLinkStyle : linkStyle}
        >
          クラスタリング
        </NavLink>
      </nav>
      <main style={{ padding: '2rem', maxWidth: '860px', margin: '0 auto' }}>
        <Routes>
          <Route path="/" element={<RecommendationPage />} />
          <Route path="/sentiment" element={<SentimentPage />} />
          <Route path="/timeseries" element={<TimeseriesPage />} />
          <Route path="/clustering" element={<ClusteringPage />} />
        </Routes>
      </main>
    </BrowserRouter>
  )
}
