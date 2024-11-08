import React, { useState } from 'react';
import useCriterion from '../hooks/useCriterion';

const HRInterface = () => {
  const { criteria, newCriterion, setNewCriterion, addCriterion, removeCriterion, loading } = useCriterion();
  const [weights, setWeights] = useState({});

  const updateWeight = (index, weight) => {
    setWeights({ ...weights, [index]: weight });
  };

  return (
    <div>
      <h2>HR Interface for Criteria Management</h2>
      <div>
        <input
          type="text"
          value={newCriterion}
          onChange={(e) => setNewCriterion(e.target.value)}
          placeholder="Enter new criterion"
        />
        <button onClick={addCriterion} disabled={loading}>
          {loading ? 'Adding...' : 'Add Criterion'}
        </button>
      </div>
      {loading && <p>Loading...</p>}
      <ul>
        {criteria.map((criterion, index) => (
          <li key={index}>
            {criterion.name}
            <button onClick={() => removeCriterion(index)} disabled={loading}>
              {loading ? 'Removing...' : 'Remove'}
            </button>
            <input
              type="number"
              value={weights[index] || ''}
              onChange={(e) => updateWeight(index, e.target.value)}
              placeholder="Enter weight"
            />
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HRInterface;
