import React from 'react';
import { useCriterion } from '../hooks/useCriterion';

const HRInterface = () => {
  const { criteria, newCriterion, setNewCriterion, addCriterion, removeCriterion } = useCriterion();
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
