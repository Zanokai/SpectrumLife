<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SpectrumLife - La tua vita su misura</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        /* ... [stile rimanente rimane lo stesso] ... */
    </style>
</head>
<body class="bg-gray-50 font-sans" data-theme="light">
    <!-- ... [resto del codice HTML rimane lo stesso] ... -->

    <!-- Aggiunto per completezza - il codice questo punto corrisponde a quanto fornito dall'utente -->
    <!-- ... -->

    <script>
        // User Data
        const userData = {
            // ... [dati utente rimanenti rimangono lo stesso] ...
        };

        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            updateWelcomeMessage();
            updateTaskCount();
            applyTheme();
            
            // Load user preferences from localStorage if available
            if(localStorage.getItem('spectrumLifeUserData')) {
                const savedData = JSON.parse(localStorage.getItem('spectrumLifeUserData'));
                Object.assign(userData, savedData);
                applyUserSettings();
            }
            
            // Initialize event listeners
            initEventListeners();
        });

        // Apply user settings to interface
        function applyUserSettings() {
            // Theme
            document.body.setAttribute('data-theme', userData.theme);
            
            // Font size
            document.documentElement.style.setProperty('--text-font-size', userData.fontSize + 'px');
            
            // Animations
            if (userData.reduceAnimations) {
                document.body.classList.add('reduce-motion');
            } else {
                document.body.classList.remove('reduce-motion');
            }
            
            // Sensitivity sliders
            document.getElementById('lightSensitivity').value = userData.lightSensitivity;
            document.getElementById('soundSensitivity').value = userData.soundSensitivity;
            
            // Theme toggle
            if (userData.autoDarkMode) {
                // Add logic for automatic dark mode based on time/circumstances
            }
            
            // Sensory overload mode
            if (userData.sensoryOverloadMode) {
                document.body.classList.add('sensory-overload');
            } else {
                document.body.classList.remove('sensory-overload');
            }
            
            // Social scripts detail level
            document.getElementById('socialDetailLevel').value = userData.socialDetailLevel;
            
            // Social tips visibility
            document.getElementById('showSocialTips').checked = userData.showSocialTips;
            
            // Task management
            document.getElementById('maxDailyTasks').value = userData.maxDailyTasks;
            document.getElementById('dayDivision').value = userData.dayDivision;
            document.getElementById('showTaskReminders').checked = userData.showTaskReminders;
        }

        // Apply theme based on user preference
        function applyTheme() {
            document.body.setAttribute('data-theme', userData.theme);
        }

        // Initialize all event listeners
        function initEventListeners() {
            // ... [resto degli ascoltatori eventi rimangono lo stesso] ...

            // Theme selection
            document.querySelectorAll('.color-option').forEach(option => {
                option.addEventListener('click', function() {
                    document.querySelectorAll('.color-option').forEach(opt => opt.classList.remove('selected'));
                    this.classList.add('selected');
                    userData.theme = this.getAttribute('data-theme');
                    applyTheme();
                    
                    // Update localStorage
                    localStorage.setItem('spectrumLifeUserData', JSON.stringify(userData));
                });
            });
            
            // Font size slider
            document.getElementById('fontSizeSlider').addEventListener('input', function() {
                userData.fontSize = this.value;
                document.documentElement.style.setProperty('--text-font-size', userData.fontSize + 'px');
                
                // Update localStorage
                localStorage.setItem('spectrumLifeUserData', JSON.stringify(userData));
            });
            
            // Reduce animations checkbox
            document.getElementById('reduceAnimations').addEventListener('change', function() {
                userData.reduceAnimations = this.checked;
                if (userData.reduceAnimations) {
                    document.body.classList.add('reduce-motion');
                } else {
                    document.body.classList.remove('reduce-motion');
                }
                
                // Update localStorage
                localStorage.setItem('spectrumLifeUserData', JSON.stringify(userData));
            });
            
            // Light sensitivity slider
            document.getElementById('lightSensitivity').addEventListener('input', function() {
                userData.lightSensitivity = this.value;
                
                // Update localStorage
                localStorage.setItem('spectrumLifeUserData', JSON.stringify(userData));
            });
            
            // Sound sensitivity slider
            document.getElementById('soundSensitivity').addEventListener('input', function() {
                userData.soundSensitivity = this.value;
                
                // Update localStorage
                localStorage.setItem('spectrumLifeUserData', JSON.stringify(userData));
            });
            
            // Dark mode toggle
            document.getElementById('darkModeToggle').addEventListener('change', function() {
                userData.autoDarkMode = this.checked;
                
                // Update localStorage
                localStorage.setItem('spectrumLifeUserData', JSON.stringify(userData));
            });
            
            // Sensory overload mode toggle
            document.getElementById('sensoryOverloadMode').addEventListener('change', function() {
                userData.sensoryOverloadMode = this.checked;
                if (userData.sensoryOverloadMode) {
                    document.body.classList.add('sensory-overload');
                } else {
                    document.body.classList.remove('sensory-overload');
                }
                
                // Update localStorage
                localStorage.setItem('spectrumLifeUserData', JSON.stringify(userData));
            });
            
            // Social detail level slider
            document.getElementById('socialDetailLevel').addEventListener('input', function() {
                userData.socialDetailLevel = this.value;
                
                // Update localStorage
                localStorage.setItem('spectrumLifeUserData', JSON.stringify(userData));
            });
            
            // Show social tips checkbox
            document.getElementById('showSocialTips').addEventListener('change', function() {
                userData.showSocialTips = this.checked;
                
                // Update localStorage
                localStorage.setItem('spectrumLifeUserData', JSON.stringify(userData));
            });
            
            // Max daily tasks input
            document.getElementById('maxDailyTasks').addEventListener('input', function() {
                userData.maxDailyTasks = this.value;
                
                // Update localStorage
                localStorage.setItem('spectrumLifeUserData', JSON.stringify(userData));
            });
            
            // Day division select
            document.getElementById('dayDivision').addEventListener('change', function() {
                userData.dayDivision = this.value;
                
                // Update localStorage
                localStorage.setItem('spectrumLifeUserData', JSON.stringify(userData));
            });
            
            // Show task reminders checkbox
            document.getElementById('showTaskReminders').addEventListener('change', function() {
                userData.showTaskReminders = this.checked;
                
                // Update localStorage
                localStorage.setItem('spectrumLifeUserData', JSON.stringify(userData));
            });
        }
    </script>
</body>
</html>