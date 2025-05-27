class SubjectDetector:
    @staticmethod
    def detect_subject(text):
        """Detects subject based on keywords in text"""
        subject_keywords = {
            'Physics': ['newton', 'force', 'acceleration', 'velocity', 'momentum', 
                      'energy', 'quantum', 'relativity'],
            'Biology': ['photosynthesis', 'cell', 'dna', 'organism', 'evolution',
                      'ecosystem', 'respiration'],
            'Chemistry': ['atom', 'molecule', 'reaction', 'acid', 'base',
                        'periodic table', 'bond'],
            'Mathematics': ['algebra', 'calculus', 'equation', 'geometry',
                          'derivative', 'integral', 'matrix'],
            'History': ['war', 'revolution', 'empire', 'ancient', 'medieval',
                       'renaissance', 'civilization'],
            'Computer Science': ['programming', 'algorithm', 'database', 'network',
                               'software', 'compiler']
        }
        
        text = text.lower()
        for subject, keywords in subject_keywords.items():
            if any(keyword in text for keyword in keywords):
                return subject
        
        return 'General'