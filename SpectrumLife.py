<!DOCTYPE html>
<html lang="it">
<head>
    <!-- Testa rimasta invariata -->
</head>
<body class="bg-gray-50 font-sans" data-theme="light">
    <!-- Tutto il corpo HTML rimasto invariato -->

    <script>
        // User Data
        const userData = {
            name: "Alex",
            age: 24,
            supportLevel: "medium",
            theme: "light",
            fontSize: 16,
            reduceAnimations: false,
            lightSensitivity: 3,
            soundSensitivity: 4,
            autoDarkMode: false,
            sensoryOverloadMode: false,
            socialDetailLevel: 3,
            showSocialTips: true,
            maxDailyTasks: 8,
            dayDivision: "3",
            showTaskReminders: true,
            selectedTools: ["rain", "breathing", "drawing", "pressure"],
            socialScripts: [
                "Come rispondere a 'Come stai?'",
                "Cosa dire quando non capisco",
                "Come chiedere una pausa"
            ],
            helpOptions: [
                "Pausa sensoriale",
                "Stimming",
                "Oggetto confort",
                "Respirazione",
                "Spazio tranquillo",
                "Pressione profonda"
            ]
        };

        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            updateWelcomeMessage();
            updateTaskCount();
            applyUserSettings();
            
            if(localStorage.getItem('spectrumLifeUserData')) {
                const savedData = JSON.parse(localStorage.getItem('spectrumLifeUserData'));
                Object.assign(userData, savedData);
                applyUserSettings();
            }
            
            initEventListeners();
            loadSocialScripts();
            loadCalmingTools();
            loadHelpOptions();
        });

        function initEventListeners() {
            // ... Altri listener rimasti invariati ...

            // Drag and drop per strumenti calmanti
            setupDragAndDrop();

            // Edit Help Options Modal
            const editHelpOptionsBtn = document.getElementById('editHelpOptionsBtn');
            const editHelpOptionsModal = document.getElementById('editHelpOptionsModal');
            const closeEditHelpOptionsModal = document.getElementById('closeEditHelpOptionsModal');
            const cancelEditHelpOptions = document.getElementById('cancelEditHelpOptions');
            const saveHelpOptions = document.getElementById('saveHelpOptions');
            const addNewHelpOption = document.getElementById('addNewHelpOption');
            const helpOptionsEditContainer = document.getElementById('helpOptionsEditContainer');

            editHelpOptionsBtn.addEventListener('click', function() {
                helpOptionsEditContainer.innerHTML = '';
                userData.helpOptions.forEach(option => {
                    const div = document.createElement('div');
                    div.className = 'flex items-center space-x-2';
                    div.innerHTML = `
                        <input type="text" class="flex-1 p-2 border border-gray-300 rounded" value="${option}">
                        <button class="p-2 text-red-500 hover:text-red-700 remove-help-option">
                            <i class="fas fa-trash"></i>
                        </button>
                    `;
                    helpOptionsEditContainer.appendChild(div);
                });
                editHelpOptionsModal.classList.remove('hidden');
            });

            addNewHelpOption.addEventListener('click', function() {
                const div = document.createElement('div');
                div.className = 'flex items-center space-x-2';
                div.innerHTML = `
                    <input type="text" class="flex-1 p-2 border border-gray-300 rounded" placeholder="Nuova opzione">
                    <button class="p-2 text-red-500 hover:text-red-700 remove-help-option">
                        <i class="fas fa-trash"></i>
                    </button>
                `;
                helpOptionsEditContainer.appendChild(div);
            });

            helpOptionsEditContainer.addEventListener('click', function(e) {
                if(e.target.closest('.remove-help-option')) {
                    e.target.closest('.flex').remove();
                }
            });

            saveHelpOptions.addEventListener('click', function() {
                userData.helpOptions = Array.from(helpOptionsEditContainer.querySelectorAll('input')).map(input => input.value);
                localStorage.setItem('spectrumLifeUserData', JSON.stringify(userData));
                loadHelpOptions();
                editHelpOptionsModal.classList.add('hidden');
            });

            // ... Altri listener per modali ...
        }

        function applyUserSettings() {
            applyTheme();
            updateFontSize();
            toggleAnimations();
            updateSensorySettings();
            updateSocialSettings();
            updateTaskSettings();
            updateAccessibility();
        }

        function applyTheme() {
            document.body.setAttribute('data-theme', userData.theme);
            if(userData.autoDarkMode) {
                const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                document.body.setAttribute('data-theme', isDark ? 'dark' : 'light');
            }
            
            if(userData.sensoryOverloadMode) {
                document.body.classList.add('sensory-overload');
            } else {
                document.body.classList.remove('sensory-overload');
            }
        }

        function updateFontSize() {
            document.body.style.fontSize = `${userData.fontSize}px`;
        }

        function toggleAnimations() {
            if(userData.reduceAnimations) {
                document.body.classList.add('reduce-motion');
            } else {
                document.body.classList.remove('reduce-motion');
            }
        }

        function loadSocialScripts() {
            const container = document.getElementById('socialScriptsContainer');
            container.innerHTML = '';
            userData.socialScripts.forEach((script, index) => {
                const button = document.createElement('button');
                button.className = 'social-script-btn w-full text-left px-4 py-2 bg-white border border-gray-200 rounded-lg hover:bg-indigo-50 transition';
                button.textContent = script;
                container.appendChild(button);
            });
        }

        function loadCalmingTools() {
            const container = document.getElementById('calmingToolsContainer');
            container.innerHTML = '';
            userData.selectedTools.forEach(tool => {
                const toolData = getToolData(tool);
                const button = document.createElement('button');
                button.className = 'calming-tool-btn p-4 rounded-lg hover:bg-opacity-50 transition flex flex-col items-center';
                button.innerHTML = `
                    <i class="${toolData.icon} text-2xl mb-2"></i>
                    <span>${toolData.label}</span>
                `;
                button.style.backgroundColor = toolData.bgColor;
                container.appendChild(button);
            });
        }

        function getToolData(tool) {
            const tools = {
                rain: { icon: 'fas fa-cloud-rain', label: 'Suoni natura', bgColor: '#dbeafe' },
                breathing: { icon: 'fas fa-feather-alt', label: 'Respirazione', bgColor: '#d1fae5' },
                drawing: { icon: 'fas fa-palette', label: 'Disegno', bgColor: '#e9d5ff' },
                pressure: { icon: 'fas fa-weight', label: 'Pressione', bgColor: '#fef3c7' },
                music: { icon: 'fas fa-music', label: 'Musica', bgColor: '#fce7f3' },
                counting: { icon: 'fas fa-sort-numeric-up', label: 'Contare', bgColor: '#fee2e2' }
            };
            return tools[tool];
        }

        function setupDragAndDrop() {
            const container = document.getElementById('selectedToolsContainer');
            
            container.addEventListener('dragstart', e => {
                if(e.target.classList.contains('selected-tool')) {
                    e.dataTransfer.setData('text/plain', e.target.dataset.tool);
                    e.target.classList.add('dragging');
                }
            });

            container.addEventListener('dragover', e => {
                e.preventDefault();
                const afterElement = getDragAfterElement(container, e.clientY);
                const draggable = document.querySelector('.dragging');
                if(afterElement == null) {
                    container.appendChild(draggable);
                } else {
                    container.insertBefore(draggable, afterElement);
                }
            });

            container.addEventListener('dragend', e => {
                e.target.classList.remove('dragging');
                // Aggiorna l'ordine nello userData
                userData.selectedTools = Array.from(container.children).map(child => child.dataset.tool);
                localStorage.setItem('spectrumLifeUserData', JSON.stringify(userData));
            });
        }

        function getDragAfterElement(container, y) {
            const draggableElements = [...container.querySelectorAll('.selected-tool:not(.dragging)')];
            
            return draggableElements.reduce((closest, child) => {
                const box = child.getBoundingClientRect();
                const offset = y - box.top - box.height / 2;
                if(offset < 0 && offset > closest.offset) {
                    return { offset: offset, element: child };
                } else {
                    return closest;
                }
            }, { offset: Number.NEGATIVE_INFINITY }).element;
        }

        function loadHelpOptions() {
            const container = document.getElementById('moodHelpOptions');
            container.innerHTML = '';
            userData.helpOptions.forEach(option => {
                const button = document.createElement('button');
                button.className = 'mood-help-btn px-3 py-2 rounded-lg hover:bg-indigo-200 transition text-sm';
                button.textContent = option;
                button.style.backgroundColor = '#c7d2fe';
                container.appendChild(button);
            });
        }

        // ... Resto delle funzioni di utilità ...
    </script>
</body>
</html>
