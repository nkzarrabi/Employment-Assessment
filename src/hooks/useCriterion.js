import { useState } from 'react';

export const useCriterion = (initialCriteria = [], initialNewCriterion = '') => {
  const [criteria, setCriteria] = useState(initialCriteria);
  const [newCriterion, setNewCriterion] = useState(initialNewCriterion);

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

  return { criteria, newCriterion, setNewCriterion, addCriterion, removeCriterion };
};
