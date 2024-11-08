import { useState, useEffect } from 'react';
import axios from 'axios';

const useCriterion = (initialCriteria = [], initialNewCriterion = '') => {
  const [criteria, setCriteria] = useState(initialCriteria);
  const [newCriterion, setNewCriterion] = useState(initialNewCriterion);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchCriteria = async () => {
      setLoading(true);
      try {
        const response = await axios.get('/api/criteria/');
        setCriteria(response.data);
      } catch (error) {
        console.error('Error fetching criteria:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchCriteria();
  }, []);

  const addCriterion = async () => {
    if (newCriterion.trim() !== '') {
      setLoading(true);
      try {
        const response = await axios.post('/api/criteria/', { name: newCriterion });
        setCriteria([...criteria, response.data]);
        setNewCriterion('');
      } catch (error) {
        console.error('Error adding criterion:', error);
      } finally {
        setLoading(false);
      }
    }
  };

  const removeCriterion = async (index) => {
    const criterionToRemove = criteria[index];
    setLoading(true);
    try {
      await axios.delete(`/api/criteria/${criterionToRemove.id}/`);
      const updatedCriteria = criteria.filter((_, i) => i !== index);
      setCriteria(updatedCriteria);
    } catch (error) {
      console.error('Error removing criterion:', error);
    } finally {
      setLoading(false);
    }
  };

  return { criteria, newCriterion, setNewCriterion, addCriterion, removeCriterion, loading };
};

export default useCriterion;
