def grades_statistics(grades):
    if not grades:  
        return {
            'average': 0,
            'best': 0,
            'worst': 0,
            'passed': 0,
            'failed': 0
        }
    
    passed = sum(1 for grade in grades if grade >= 5)
    failed = sum(1 for grade in grades if grade < 5)
    
    return {
        'average': sum(grades) / len(grades),
        'best': max(grades),
        'worst': min(grades),
        'passed': passed,
        'failed': failed
    }


grades = [8, 5, 3, 7, 10, 4, 6, 9, 2, 7]
print(grades_statistics(grades))
