
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [size, setSize] = useState('');
  const [bedrooms, setBedrooms] = useState('');
  const [price, setPrice] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const PredictPrice = async () => {
    if (!size || !bedrooms || Number(size) <= 0 || Number(bedrooms) <= 0) {
      setError('Please enter valid plot size and bedroom count.');
      setPrice(null);
      return;
    }

    try {
      setLoading(true);
      setError('');
      setPrice(null);

      const response = await axios.post(
        'http://127.0.0.1:8000/predict/',
        {
          LotArea: Number(size),
          BedroomAbvGr: Number(bedrooms)
        }
      );

      setPrice(response.data.predicted_price);

    } catch (err) {
      console.error(err);
      setError('Unable to predict price. Please check your backend server.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="prediction-card">

        <div className="icon">🏡</div>

        <h1>House Price Prediction</h1>
        <p className="subtitle">
          Enter your property details to estimate its price.
        </p>

        <div className="form-group">
          <label>Plot Size (sq ft)</label>
          <input
            type="number"
            placeholder="Enter plot size"
            value={size}
            onChange={(e) => setSize(e.target.value)}
            min="1"
          />
        </div>

        <div className="form-group">
          <label>Number of Bedrooms</label>
          <input
            type="number"
            placeholder="Enter number of bedrooms"
            value={bedrooms}
            onChange={(e) => setBedrooms(e.target.value)}
            min="1"
          />
        </div>

        <button
          className="predict-btn"
          onClick={PredictPrice}
          disabled={loading}
        >
          {loading ? 'Predicting...' : 'Predict Price →'}
        </button>

        {error && (
          <p className="error">{error}</p>
        )}

        {price !== null && (
          <div className="result">
            <p>Estimated House Price</p>
            <h2>₹{Number(price).toLocaleString('en-IN')}</h2>
          </div>
        )}

        <p className="footer">
          AI Powered House Price Estimation
        </p>

      </div>
    </div>
  );
}

export default App;
