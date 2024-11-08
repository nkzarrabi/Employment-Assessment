import { renderHook, act } from '@testing-library/react-hooks';
import { useCriterion } from './useCriterion';

describe('useCriterion', () => {
  it('should initialize with default values', () => {
    const { result } = renderHook(() => useCriterion());

    expect(result.current.criteria).toEqual([]);
    expect(result.current.newCriterion).toBe('');
  });

  it('should initialize with provided values', () => {
    const initialCriteria = ['criterion1', 'criterion2'];
    const initialNewCriterion = 'newCriterion';
    const { result } = renderHook(() => useCriterion(initialCriteria, initialNewCriterion));

    expect(result.current.criteria).toEqual(initialCriteria);
    expect(result.current.newCriterion).toBe(initialNewCriterion);
  });

  it('should add a new criterion', () => {
    const { result } = renderHook(() => useCriterion());

    act(() => {
      result.current.setNewCriterion('newCriterion');
    });

    act(() => {
      result.current.addCriterion();
    });

    expect(result.current.criteria).toEqual(['newCriterion']);
    expect(result.current.newCriterion).toBe('');
  });

  it('should not add an empty criterion', () => {
    const { result } = renderHook(() => useCriterion());

    act(() => {
      result.current.setNewCriterion('  ');
    });

    act(() => {
      result.current.addCriterion();
    });

    expect(result.current.criteria).toEqual([]);
    expect(result.current.newCriterion).toBe('  ');
  });

  it('should remove a criterion', () => {
    const initialCriteria = ['criterion1', 'criterion2'];
    const { result } = renderHook(() => useCriterion(initialCriteria));

    act(() => {
      result.current.removeCriterion(0);
    });

    expect(result.current.criteria).toEqual(['criterion2']);
  });
});
