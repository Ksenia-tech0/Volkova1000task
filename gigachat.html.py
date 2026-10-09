<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FreePyCamp — Курс Python в одном файле</title>
    <script src="https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.js"></script>
    <style>
        :root { --bg: #1e1e1e; --card: #2d2d30; --text: #d4d4d4; --accent: #007acc; --success: #4caf50; --error: #f44336; }
        * { box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 0; background: var(--bg); color: var(--text); line-height: 1.6; }
        .sidebar { position: fixed; top: 0; left: 0; width: 280px; height: 100vh; background: #252526; overflow-y: auto; border-right: 1px solid #333; padding: 20px; }
        .sidebar h2 { margin-top: 0; font-size: 1.2rem; color: #fff; }
        .module-title { font-weight: bold; color: #fff; padding: 10px 0 5px; font-size: 1.1rem; cursor: pointer; user-select: none; }
        .module-title.completed { color: var(--success); }
        .lesson-item { padding: 8px 15px; margin: 2px 0; border-radius: 4px; cursor: pointer; font-size: 0.95rem; }
        .lesson-item.active { background: var(--accent); color: #fff; }
        .lesson-item:not(.active):hover { background: #333; }
        .main-content { margin-left: 280px; padding: 30px; max-width: 1200px; }
        .lesson-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .lesson-header h1 { margin: 0; color: #fff; }
        .progress-text { font-size: 0.9rem; color: #aaa; }
        .content-columns { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .panel { background: var(--card); border-radius: 8px; padding: 20px; border: 1px solid #333; }
        .panel h3 { margin-top: 0; color: #fff; }
        textarea, pre { width: 100%; height: 300px; font-family: "Consolas", "Monaco", monospace; font-size: 14px; border-radius: 4px; border: 1px solid #333; background: #1e1e1e; color: #d4d4d4; }
        textarea { padding: 10px; resize: vertical; }
        pre { padding: 10px; white-space: pre-wrap; word-wrap: break-word; overflow-y: auto; }
        button { background: var(--accent); color: #fff; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-size: 1rem; margin-right: 10px; }
        button:hover { background: #005a99; }
        button.danger { background: var(--error); }
        button.danger:hover { background: #c62828; }
        button.success { background: var(--success); }
        button.success:hover { background: #388e3c; }
        .output-box { margin-top: 10px; min-height: 40px; }
        .test-box { margin-top: 10px; padding: 10px; border-radius: 4px; display: none; }
        .test-box.success { background: #2e7d32; color: #fff; display: block; }
        .test-box.error { background: var(--error); color: #fff; display: block; }
        .hidden { display: none; }
        .status-dot { display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: #555; margin-right: 8px; }
        .status-dot.done { background: var(--success); }
        @media (max-width: 900px) { .content-columns { grid-template-columns: 1fr; } .sidebar { width: 220px; } .main-content { margin-left: 220px; } }
    </style>
</head>
<body>

<div class="sidebar">
    <h2>FreePyCamp</h2>
    <div id="curriculum"></div>
    <div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #333; font-size: 0.8rem; color: #888;">
        Выполнено: <span id="progress-count">0</span>/<span id="total-lessons">0</span>
    </div>
</div>

<div class="main-content">
    <div class="lesson-header">
        <h1 id="lesson-title">Выберите урок</h1>
        <div class="progress-text" id="lesson-progress"></div>
    </div>

    <div id="lesson-content">
        <!-- Сюда динамически загружается контент -->
    </div>
</div>

<script>
// === БАЗА ДАННЫХ КУРСА ===
const curriculum = [
    {
        id: 1, title: "Основы и переменные", lessons: [
            {id: 1, title: "Hello, World!", theory: "Функция print() выводит данные в консоль.", task: "Выведите на экран фразу 'Привет, мир!'", tests: "print('Привет, мир!')"},
            {id: 2, title: "Переменные и типы", theory: "Переменные создаются при присваивании. Основные типы: int, float, str, bool.", task: "Создайте переменную name со своим именем и выведите её.", tests: "name = 'Алексей'\nprint(name)"},
            {id: 3, title: "Арифметика", theory: "Python поддерживает +, -, *, /, // (целочисленное), % (остаток), ** (степень).", task: "Создайте переменную x = 10, y = 3. Выведите их сумму, произведение и остаток от деления.", tests: "x = 10\ny = 3\nprint(x + y)\nprint(x * y)\nprint(x % y)"}
        ]
    },
    {
        id: 2, title: "Управление потоком", lessons: [
            {id: 4, title: "Условный оператор if", theory: "if, elif, else позволяют выполнять код по условию.", task: "Создайте переменную age = 20. Если age >= 18, выведите 'Доступ разрешен'.", tests: "age = 20\nif age >= 18:\n    print('Доступ разрешен')"},
            {id: 5, title: "Цикл for", theory: "Цикл for перебирает элементы (например, в range()).", task: "С помощью цикла for выведите числа от 1 до 5.", tests: "for i in range(1, 6):\n    print(i)"},
            {id: 6, title: "Цикл while", theory: "Цикл while выполняется, пока условие истинно.", task: "Выведите числа от 5 до 1 с помощью цикла while.", tests: "i = 5\nwhile i > 0:\n    print(i)\n    i -= 1"}
        ]
    },
    {
        id: 3, title: "Структуры данных", lessons: [
            {id: 7, title: "Списки (Lists)", theory: "Списки — изменяемые упорядоченные коллекции. Индексация с 0.", task: "Создайте список fruits = ['яблоко', 'банан']. Добавьте 'груша' и выведите второй элемент.", tests: "fruits = ['яблоко', 'банан']\nfruits.append('груша')\nprint(fruits[1])"},
            {id: 8, title: "Словари (Dicts)", theory: "Словари хранят пары ключ: значение.", task: "Создайте словарь user = {'name': 'Иван', 'age': 25}. Выведите имя.", tests: "user = {'name': 'Иван', 'age': 25}\nprint(user['name'])"},
            {id: 9, title: "Кортежи (Tuples)", theory: "Кортежи — неизменяемые списки. Обозначаются ( ).", task: "Создайте кортеж point = (10, 20) и выведите его.", tests: "point = (10, 20)\nprint(point)"}
        ]
    },
    {
        id: 4, title: "Функции", lessons: [
            {id: 10, title: "Создание функций", theory: "Функции объявляются через def. Они могут возвращать значения через return.", task: "Создайте функцию sum(a, b), которая возвращает сумму аргументов. Вызовите её с (5, 10).", tests: "def sum(a, b):\n    return a + b\nprint(sum(5, 10))"},
            {id: 11, title: "Аргументы и области видимости", theory: "Аргументы могут быть со значениями по умолчанию. Переменные внутри функции локальны.", task: "Создайте функцию greet(name='Гость'), которая выводит 'Привет, {name}'. Вызовите без аргументов.", tests: "def greet(name='Гость'):\n    print(f'Привет, {name}')\ngreet()"}
        ]
    },
    {
        id: 5, title: "Файлы и завершение", lessons: [
            {id: 12, title: "Работа с файлами", theory: "Файлы открываются через open(). Используйте 'w' для записи, 'r' для чтения.", task: "Запишите строку 'Данные сохранены' в файл data.txt.", tests: "with open('data.txt', 'w') as f:\n    f.write('Данные сохранены')"},
            {id: 13, title: "Поздравляем!", theory: "Вы изучили основы Python. Этого достаточно для написания простых скриптов, парсеров и автоматизации. Дальше вас ждут ООП, библиотеки (Pandas, Requests) и фреймворки.", task: "Напишите любую программу, которая выводит 'Я освоил основы Python!'", tests: "print('Я освоил основы Python!')"}
        ]
    }
];

// === ЛОГИКА ПРИЛОЖЕНИЯ ===
let pyodide = null;
let currentModule = 0;
let currentLesson = 0;
let progress = JSON.parse(localStorage.getItem('freepycamp_progress') || '{}');

const sidebar = document.getElementById('curriculum');
const titleEl = document.getElementById('lesson-title');
const contentEl = document.getElementById('lesson-content');
const progressCount = document.getElementById('progress-count');
const totalLessons = document.getElementById('total-lessons');

// Подсчет общего числа уроков
let total = 0;
curriculum.forEach(m => total += m.lessons.length);
totalLessons.textContent = total;

function renderSidebar() {
    sidebar.innerHTML = '';
    let doneCount = 0;
    curriculum.forEach(module => {
        const modDiv = document.createElement('div');
        const modTitle = document.createElement('div');
        modTitle.className = 'module-title';
        modTitle.textContent = module.title;
        modTitle.onclick = () => {
            currentModule = module.id - 1;
            currentLesson = 0;
            saveProgress();
            loadLesson();
        };
        
        const isModuleDone = module.lessons.every(l => progress[`m${module.id}l${l.id}`]);
        if (isModuleDone) {
            modTitle.innerHTML = '<span class="status-dot done"></span>' + module.title;
            doneCount += module.lessons.length;
        }
        
        modDiv.appendChild(modTitle);
        
        module.lessons.forEach(lesson => {
            const lessonItem = document.createElement('div');
            lessonItem.className = 'lesson-item';
            lessonItem.textContent = lesson.title;
            if (progress[`m${module.id}l${lesson.id}`]) {
                lessonItem.innerHTML = '<span class="status-dot done"></span>' + lesson.title;
            }
            lessonItem.onclick = () => {
                currentModule = module.id - 1;
                currentLesson = lesson.id - 1;
                saveProgress();
                loadLesson();
            };
            modDiv.appendChild(lessonItem);
        });
        sidebar.appendChild(modDiv);
    });
    progressCount.textContent = doneCount;
}

function loadLesson() {
    const module = curriculum[currentModule];
    const lesson = module.lessons[currentLesson];
    
    // Обновляем сайдбар (подсветка активного урока)
    renderSidebar();
    document.querySelectorAll('.lesson-item').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.lesson-item').forEach(el => {
        if (el.textContent.includes(lesson.title)) el.classList.add('active');
    });

    titleEl.textContent = lesson.title;
    
    contentEl.innerHTML = `
        <div class="content-columns">
            <div class="panel">
                <h3>Теория</h3>
                <p>${lesson.theory}</p>
            </div>
            <div class="panel">
                <h3>Задание</h3>
                <p>${lesson.task}</p>
                <h3 style="margin-top: 20px;">Решение</h3>
                <textarea id="code-editor"># Напишите ваш код здесь</textarea>
                <div style="margin-top: 10px;">
                    <button onclick="runCode()">▶ Выполнить код</button>
                    <button onclick="checkSolution()" class="success">✓ Проверить решение</button>
                    <button onclick="resetEditor()" class="danger">↻ Сбросить</button>
                </div>
                <div class="output-box" id="output"></div>
                <div class="test-box" id="test-result"></div>
            </div>
        </div>
    `;
    
    // Фокус на редакторе
    setTimeout(() => document.getElementById('code-editor').focus(), 100);
}

async function initPyodide() {
    pyodide = await loadPyodide();
    // Добавляем встроенные функции для тестов
    pyodide.runPython(`
import sys
from io import StringIO

def _get_output():
    return _output.getvalue()

_output = StringIO()
sys.stdout = _output
    `);
}

function runCode() {
    const code = document.getElementById('code-editor').value;
    const outputEl = document.getElementById('output');
    outputEl.innerHTML = '<em>Выполнение...</em>';
    
    pyodide.runPython(`
_output.truncate(0)
_output.seek(0)
    `);

    try {
        pyodide.runPython(code);
        const out = pyodide.runPython('_get_output()');
        outputEl.innerHTML = '<strong>Вывод:</strong><br><pre>' + escapeHtml(out) + '</pre>';
        document.getElementById('test-result').style.display = 'none';
    } catch (err) {
        outputEl.innerHTML = '<strong class="error">Ошибка:</strong><br><pre>' + escapeHtml(err.message) + '</pre>';
    }
}

function checkSolution() {
    const userCode = document.getElementById('code-editor').value;
    const lesson = curriculum[currentModule].lessons[currentLesson];
    const testEl = document.getElementById('test-result');
    
    pyodide.runPython(`
_output.truncate(0)
_output.seek(0)
    `);

    try {
        // Сначала выполняем код пользователя
        pyodide.runPython(userCode);
        
        // Затем выполняем тесты (assert)
        pyodide.runPython(lesson.tests);
        
        testEl.className = 'test-box success';
        testEl.textContent = '✅ Отлично! Тесты пройдены.';
        testEl.style.display = 'block';
        
        // Помечаем урок как пройденный
        progress[`m${currentModule + 1}l${lesson.id}`] = true;
        saveProgress();
        renderSidebar();
    } catch (err) {
        testEl.className = 'test-box error';
        testEl.textContent = '❌ Ошибка в тестах: ' + err.message;
        testEl.style.display = 'block';
    }
}

function resetEditor() {
    const lesson = curriculum[currentModule].lessons[currentLesson];
    document.getElementById('code-editor').value = '# Напишите ваш код здесь';
    document.getElementById('output').innerHTML = '';
    document.getElementById('test-result').style.display = 'none';
}

function saveProgress() {
    localStorage.setItem('freepycamp_progress', JSON.stringify(progress));
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// === ЗАПУСК ===
initPyodide().then(() => {
    loadLesson();
});
</script>

</body>
</html>