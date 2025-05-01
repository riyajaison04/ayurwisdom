# from flask import Flask, request, jsonify
# import pickle
# import numpy as np
# from flask_cors import CORS
# from flask_cors import CORS
#   # Enable CORS for all routes


# app = Flask(__name__)
# CORS(app)

# # Load the trained model
# with open('ensemble_model.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)

# @app.route('/api/classify', methods=['POST'])
# def classify():
#     data = request.json
    
#     # Extract features from the request data using the latest feature names
#     features = np.array([
#         data['Age'],
#         data['Gender'],
#         data['Height'],
#         data['Weight'],
#         data['Skin'],
#         data['Frame'],
#         data['Digestion'],
#         data['Mood'],
#         data['Sleep'],
#         data['Temperament'],
#         data['Sensitivity'],
#         data['Face_Shape'],
#         data['Activity'],
#         data['Dietary_Choices'],
#         data['Hair'],
#         data['Climate'],
#         data['Emotion'],
#         data['Sleep_Quality'],
#         data['Stress_Reaction'],
#         data['Agility'],
#         data['Appetite'],
#         data['Body_Temperature']
#     ]).reshape(1, -1)  # Reshape for a single sample prediction

#     # Make prediction
#     predicted_dosha = model.predict(features)[0]

#     # Suggestions based on dosha
#     suggestions = {
#         'Vata': {
#             'food': 'Warm, nourishing foods like soups and stews.',
#             'lifestyle': 'Regular routines and gentle exercises.',
#             'career': 'Creative fields or roles requiring flexibility.',
#             'precautions': 'Stay warm and avoid cold and dry conditions.',
#             'emotional_state': 'Tend to feel anxious; practice grounding activities.',
#             'exercise': 'Yoga and Pilates; gentle activities.',
#             'yoga': 'Focus on grounding poses like Mountain and Warrior.'
#         },
#         'Pitta': {
#             'food': 'Cooling foods like salads and fruits.',
#             'lifestyle': 'Balanced routines with relaxation techniques.',
#             'career': 'Leadership roles or fields requiring decisiveness.',
#             'precautions': 'Avoid overheating; stay cool.',
#             'emotional_state': 'May experience irritability; find calming practices.',
#             'exercise': 'Moderate activities like swimming or cycling.',
#             'yoga': 'Incorporate calming poses like Forward Bend and Child’s Pose.'
#         },
#         'Kapha': {
#             'food': 'Light, dry foods; limit heavy and oily items.',
#             'lifestyle': 'Regular activity and mental stimulation.',
#             'career': 'Supportive roles or those requiring patience.',
#             'precautions': 'Avoid damp and heavy environments.',
#             'emotional_state': 'Tend towards lethargy; engage in motivating activities.',
#             'exercise': 'Vigorous activities like running or dancing.',
#             'yoga': 'Focus on energizing poses like Sun Salutations and Backbends.'
#         },
#         'Vata-Pitta': {
#             'food': 'Balanced meals with both warming and cooling ingredients.',
#             'lifestyle': 'Structured yet flexible routines.',
#             'career': 'Creative and analytical roles.',
#             'precautions': 'Maintain balance between heating and cooling factors.',
#             'emotional_state': 'May feel conflicted; practice mindfulness.',
#             'exercise': 'Combination of yoga and moderate cardio.',
#             'yoga': 'Blend of calming and invigorating poses.'
#         },
#         'Pitta-Kapha': {
#             'food': 'Cooling yet light meals; avoid heavy foods.',
#             'lifestyle': 'Moderation with a focus on relaxation.',
#             'career': 'Roles in management or strategy.',
#             'precautions': 'Balance passion with calmness.',
#             'emotional_state': 'May feel sluggish; aim for energizing practices.',
#             'exercise': 'Mix of light cardio and strength training.',
#             'yoga': 'Focus on dynamic and restorative poses.'
#         },
#         'Vata-Kapha': {
#             'food': 'Warm and light meals; avoid cold and heavy items.',
#             'lifestyle': 'Structured routines with light activity.',
#             'career': 'Supportive roles; good in healthcare or wellness.',
#             'precautions': 'Stay warm and active; avoid stagnation.',
#             'emotional_state': 'May feel unmotivated; engage in inspiring activities.',
#             'exercise': 'Gentle activities like walking or yoga.',
#             'yoga': 'Focus on grounding and gentle poses.'
#         },
#         'Vata-Pitta-Kapha': {
#             'food': 'Diverse meals with a balance of all tastes.',
#             'lifestyle': 'Flexibility with structure; adapt as needed.',
#             'career': 'Versatile roles; good at multitasking.',
#             'precautions': 'Stay balanced in all aspects of life.',
#             'emotional_state': 'May experience emotional highs and lows; practice balance.',
#             'exercise': 'Mix of vigorous and calming activities.',
#             'yoga': 'Blend of restorative and dynamic poses.'
#         }
#     }

#     # Get suggestions based on predicted dosha
#     dosha_suggestions = suggestions.get(predicted_dosha, {})

#     return jsonify({
#         'dosha': predicted_dosha,
#         'suggestions': dosha_suggestions
#     })

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)  # Corrected _name_ to __name__
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)  # Allow credentials
# Load the trained model
with open('ensemble_model.pickle', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/api/classify', methods=['POST'])
def classify():
    # Check if request contains JSON data
    if request.is_json:
        data = request.json

        # Extract features from the request data
        features = np.array([
            data.get('Age'),
            data.get('Gender'),
            data.get('Height'),
            data.get('Weight'),
            data.get('Skin'),
            data.get('Frame'),
            data.get('Digestion'),
            data.get('Mood'),
            data.get('Sleep'),
            data.get('Temperament'),
            data.get('Sensitivity'),
            data.get('Face_Shape'),
            data.get('Activity'),
            data.get('Dietary_Choices'),
            data.get('Hair'),
            data.get('Climate'),
            data.get('Emotion'),
            data.get('Sleep_Quality'),
            data.get('Stress_Reaction'),
            data.get('Agility'),
            data.get('Appetite'),
            data.get('Body_Temperature')
        ]).reshape(1, -1)  # Reshape for a single sample prediction

        # Make prediction
        predicted_dosha = model.predict(features)[0]

        # Suggestions based on dosha
        suggestions = {
            'Vata': {
                'food': 'Warm, nourishing foods like soups and stews.',
                'lifestyle': 'Regular routines and gentle exercises.',
                'career': 'Creative fields or roles requiring flexibility.',
                'precautions': 'Stay warm and avoid cold and dry conditions.',
                'emotional_state': 'Tend to feel anxious; practice grounding activities.',
                'exercise': 'Yoga and Pilates; gentle activities.',
                'yoga': 'Focus on grounding poses like Mountain and Warrior.'
            },
            'Pitta': {
                'food': 'Cooling foods like salads and fruits.',
                'lifestyle': 'Balanced routines with relaxation techniques.',
                'career': 'Leadership roles or fields requiring decisiveness.',
                'precautions': 'Avoid overheating; stay cool.',
                'emotional_state': 'May experience irritability; find calming practices.',
                'exercise': 'Moderate activities like swimming or cycling.',
                'yoga': 'Incorporate calming poses like Forward Bend and Child’s Pose.'
            },
            'Kapha': {
                'food': 'Light, dry foods; limit heavy and oily items.',
                'lifestyle': 'Regular activity and mental stimulation.',
                'career': 'Supportive roles or those requiring patience.',
                'precautions': 'Avoid damp and heavy environments.',
                'emotional_state': 'Tend towards lethargy; engage in motivating activities.',
                'exercise': 'Vigorous activities like running or dancing.',
                'yoga': 'Focus on energizing poses like Sun Salutations and Backbends.'
            },
            'Vata-Pitta': {
                'food': 'Balanced meals with both warming and cooling ingredients.',
                'lifestyle': 'Structured yet flexible routines.',
                'career': 'Creative and analytical roles.',
                'precautions': 'Maintain balance between heating and cooling factors.',
                'emotional_state': 'May feel conflicted; practice mindfulness.',
                'exercise': 'Combination of yoga and moderate cardio.',
                'yoga': 'Blend of calming and invigorating poses.'
            },
            'Pitta-Kapha': {
                'food': 'Cooling yet light meals; avoid heavy foods.',
                'lifestyle': 'Moderation with a focus on relaxation.',
                'career': 'Roles in management or strategy.',
                'precautions': 'Balance passion with calmness.',
                'emotional_state': 'May feel sluggish; aim for energizing practices.',
                'exercise': 'Mix of light cardio and strength training.',
                'yoga': 'Focus on dynamic and restorative poses.'
            },
            'Vata-Kapha': {
                'food': 'Warm and light meals; avoid cold and heavy items.',
                'lifestyle': 'Structured routines with light activity.',
                'career': 'Supportive roles; good in healthcare or wellness.',
                'precautions': 'Stay warm and active; avoid stagnation.',
                'emotional_state': 'May feel unmotivated; engage in inspiring activities.',
                'exercise': 'Gentle activities like walking or yoga.',
                'yoga': 'Focus on grounding and gentle poses.'
            },
            'Vata-Pitta-Kapha': {
                'food': 'Diverse meals with a balance of all tastes.',
                'lifestyle': 'Flexibility with structure; adapt as needed.',
                'career': 'Versatile roles; good at multitasking.',
                'precautions': 'Stay balanced in all aspects of life.',
                'emotional_state': 'May experience emotional highs and lows; practice balance.',
                'exercise': 'Mix of vigorous and calming activities.',
                'yoga': 'Blend of restorative and dynamic poses.'
            }
        }

        # Get suggestions based on predicted dosha
        dosha_suggestions = suggestions.get(predicted_dosha, {})

        return jsonify({
            'dosha': predicted_dosha,
            'suggestions': dosha_suggestions
        })
    else:
        return jsonify({'error': 'Request must be JSON'}), 400  # Return error if not JSON

if __name__ == '__main__':  # Corrected _name_ to __name__
    app.run(debug=True, port=5000)

# from flask import Flask, request, jsonify
# import numpy as np
# from flask_cors import CORS
# import random

# app = Flask(__name__)
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

# # List of possible doshas
# doshas = ['Vata', 'Pitta', 'Kapha', 'Vata-Pitta', 'Pitta-Kapha', 'Vata-Kapha', 'Vata-Pitta-Kapha']

# # Suggestions based on dosha
# suggestions = {
#     'Vata': {
#         'food': 'Warm, nourishing foods like soups and stews.',
#         'lifestyle': 'Regular routines and gentle exercises.',
#         'career': 'Creative fields or roles requiring flexibility.',
#         'precautions': 'Stay warm and avoid cold and dry conditions.',
#         'emotional_state': 'Tend to feel anxious; practice grounding activities.',
#         'exercise': 'Yoga and Pilates; gentle activities.',
#         'yoga': 'Focus on grounding poses like Mountain and Warrior.'
#     },
#     'Pitta': {
#         'food': 'Cooling foods like salads and fruits.',
#         'lifestyle': 'Balanced routines with relaxation techniques.',
#         'career': 'Leadership roles or fields requiring decisiveness.',
#         'precautions': 'Avoid overheating; stay cool.',
#         'emotional_state': 'May experience irritability; find calming practices.',
#         'exercise': 'Moderate activities like swimming or cycling.',
#         'yoga': 'Incorporate calming poses like Forward Bend and Child’s Pose.'
#     },
#     'Kapha': {
#         'food': 'Light, dry foods; limit heavy and oily items.',
#         'lifestyle': 'Regular activity and mental stimulation.',
#         'career': 'Supportive roles or those requiring patience.',
#         'precautions': 'Avoid damp and heavy environments.',
#         'emotional_state': 'Tend towards lethargy; engage in motivating activities.',
#         'exercise': 'Vigorous activities like running or dancing.',
#         'yoga': 'Focus on energizing poses like Sun Salutations and Backbends.'
#     },
#     'Vata-Pitta': {
#         'food': 'Balanced meals with both warming and cooling ingredients.',
#         'lifestyle': 'Structured yet flexible routines.',
#         'career': 'Creative and analytical roles.',
#         'precautions': 'Maintain balance between heating and cooling factors.',
#         'emotional_state': 'May feel conflicted; practice mindfulness.',
#         'exercise': 'Combination of yoga and moderate cardio.',
#         'yoga': 'Blend of calming and invigorating poses.'
#     },
#     'Pitta-Kapha': {
#         'food': 'Cooling yet light meals; avoid heavy foods.',
#         'lifestyle': 'Moderation with a focus on relaxation.',
#         'career': 'Roles in management or strategy.',
#         'precautions': 'Balance passion with calmness.',
#         'emotional_state': 'May feel sluggish; aim for energizing practices.',
#         'exercise': 'Mix of light cardio and strength training.',
#         'yoga': 'Focus on dynamic and restorative poses.'
#     },
#     'Vata-Kapha': {
#         'food': 'Warm and light meals; avoid cold and heavy items.',
#         'lifestyle': 'Structured routines with light activity.',
#         'career': 'Supportive roles; good in healthcare or wellness.',
#         'precautions': 'Stay warm and active; avoid stagnation.',
#         'emotional_state': 'May feel unmotivated; engage in inspiring activities.',
#         'exercise': 'Gentle activities like walking or yoga.',
#         'yoga': 'Focus on grounding and gentle poses.'
#     },
#     'Vata-Pitta-Kapha': {
#         'food': 'Diverse meals with a balance of all tastes.',
#         'lifestyle': 'Flexibility with structure; adapt as needed.',
#         'career': 'Versatile roles; good at multitasking.',
#         'precautions': 'Stay balanced in all aspects of life.',
#         'emotional_state': 'May experience emotional highs and lows; practice balance.',
#         'exercise': 'Mix of vigorous and calming activities.',
#         'yoga': 'Blend of restorative and dynamic poses.'
#     }
# }

# @app.route('/api/classify', methods=['POST'])
# def classify():
#     # Check if request contains JSON data
#     if request.is_json:
#         data = request.json

#         # Randomly select a dosha
#         predicted_dosha = random.choice(doshas)

#         # Get suggestions based on predicted dosha
#         dosha_suggestions = suggestions.get(predicted_dosha, {})

#         return jsonify({
#             'dosha': predicted_dosha,
#             'suggestions': dosha_suggestions
#         })
#     else:
#         return jsonify({'error': 'Request must be JSON'}), 400

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
