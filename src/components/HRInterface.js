import React, { useState } from 'react';

const HRInterface = () => {
  const [criteria, setCriteria] = useState([]);
  const [newCriterion, setNewCriterion] = useState('');
  const [weights, setWeights] = useState({});

  const addCriterion = () => {
    if (newCriterion.trim() !== '') {
      setCriteria([...criteria, newCriterion]);
      setNewCriterion('');
    }
  };

  const removeCriterion = (index) => {
    const updatedCriteria = criteria.filter((_, i) => i !== index);
    setCriteria(updatedCriteria);
  };

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
        <button onClick={addCriterion}>Add Criterion</button>
      </div>
      <ul>
        {criteria.map((criterion, index) => (
          <li key={index}>
            {criterion}
            <button onClick={() => removeCriterion(index)}>Remove</button>
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
