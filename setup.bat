@echo off
echo 🚀 Setting up Tailwind CSS for Sunny Kids website...
echo.

:: Tạo thư mục nếu chưa có
if not exist "static\css" mkdir static\css
if not exist "static\js" mkdir static\js
if not exist "templates\components" mkdir templates\components

:: Tạo package.json
echo 🔧 Creating package.json...
(
echo {
echo   "name": "mamnon-website",
echo   "version": "1.0.0",
echo   "description": "Mam Non Website with Tailwind CSS",
echo   "scripts": {
echo     "build-css": "tailwindcss -i ./static/css/input.css -o ./static/css/style.css --watch",
echo     "build-css-prod": "tailwindcss -i ./static/css/input.css -o ./static/css/style.css --minify",
echo     "dev": "tailwindcss -i ./static/css/input.css -o ./static/css/style.css --watch"
echo   },
echo   "devDependencies": {
echo     "tailwindcss": "^3.4.0",
echo     "@tailwindcss/forms": "^0.5.7",
echo     "@tailwindcss/typography": "^0.5.10"
echo   }
echo }
) > package.json

:: Tạo tailwind.config.js
echo 🎨 Creating tailwind.config.js...
(
echo module.exports = {
echo   content: [
echo     './templates/**/*.html',
echo     './apps/**/templates/**/*.html',
echo     './static/js/**/*.js',
echo   ],
echo   theme: {
echo     extend: {
echo       colors: {
echo         'sunny-pink': '#FF6B9D',
echo         'sunny-blue': '#4ECDC4', 
echo         'sunny-yellow': '#FFE066',
echo         'sunny-green': '#44A08D',
echo         'sunny-purple': '#9B59B6',
echo         'sunny-orange': '#FF8A65',
echo       },
echo       fontFamily: {
echo         'sans': ['Inter', 'ui-sans-serif', 'system-ui'],
echo         'display': ['Poppins', 'ui-sans-serif', 'system-ui'],
echo       },
echo       animation: {
echo         'bounce-slow': 'bounce 3s infinite',
echo         'wiggle': 'wiggle 1s ease-in-out infinite',
echo         'float': 'float 6s ease-in-out infinite',
echo       },
echo       keyframes: {
echo         wiggle: {
echo           '0%%, 100%%': { transform: 'rotate(-3deg)' },
echo           '50%%': { transform: 'rotate(3deg)' },
echo         },
echo         float: {
echo           '0%%, 100%%': { transform: 'translateY(0px)' },
echo           '50%%': { transform: 'translateY(-20px)' },
echo         },
echo       }
echo     },
echo   },
echo   plugins: [
echo     require('@tailwindcss/forms'),
echo     require('@tailwindcss/typography'),
echo   ],
echo }
) > tailwind.config.js

:: Tạo input.css
echo 📝 Creating CSS input file...
(
echo @tailwind base;
echo @tailwind components;
echo @tailwind utilities;
echo.
echo @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap'^);
echo.
echo @layer base {
echo   html {
echo     scroll-behavior: smooth;
echo   }
echo   
echo   body {
echo     @apply font-sans antialiased;
echo   }
echo }
echo.
echo @layer components {
echo   .gradient-text {
echo     background: linear-gradient(135deg, #FF6B9D, #4ECDC4^);
echo     -webkit-background-clip: text;
echo     -webkit-text-fill-color: transparent;
echo     background-clip: text;
echo   }
echo   
echo   .glass {
echo     backdrop-filter: blur(10px^);
echo     background: rgba(255, 255, 255, 0.1^);
echo     border: 1px solid rgba(255, 255, 255, 0.2^);
echo   }
echo   
echo   .btn-sunny {
echo     @apply bg-gradient-to-r from-sunny-pink to-sunny-blue text-white 
echo            px-6 py-3 rounded-full font-semibold shadow-lg hover:shadow-xl 
echo            hover:-translate-y-1 transition-all duration-300;
echo   }
echo   
echo   .card-sunny {
echo     @apply bg-white rounded-2xl shadow-lg hover:shadow-2xl 
echo            border border-gray-100 hover:-translate-y-2 transition-all duration-300;
echo   }
echo }
) > static\css\input.css

:: Tạo main.js
echo ⚡ Creating JavaScript file...
(
echo // Main JavaScript for Sunny Kids website
echo document.addEventListener('DOMContentLoaded', function(^) {
echo     // Initialize all components
echo     initializeSlider(^);
echo     initializeMobileMenu(^);
echo     initializeAnimations(^);
echo }^);
echo.
echo function initializeSlider(^) {
echo     const slides = document.querySelectorAll('.slide'^);
echo     const dots = document.querySelectorAll('[data-slide]'^);
echo     let currentSlide = 0;
echo.
echo     function showSlide(index^) {
echo         slides.forEach(slide =^> slide.classList.remove('opacity-100'^)^);
echo         slides.forEach(slide =^> slide.classList.add('opacity-0'^)^);
echo         
echo         dots.forEach(dot =^> dot.classList.remove('bg-white'^)^);
echo         dots.forEach(dot =^> dot.classList.add('bg-white/50'^)^);
echo         
echo         if (slides[index]^) {
echo             slides[index].classList.remove('opacity-0'^);
echo             slides[index].classList.add('opacity-100'^);
echo         }
echo         
echo         if (dots[index]^) {
echo             dots[index].classList.remove('bg-white/50'^);
echo             dots[index].classList.add('bg-white'^);
echo         }
echo     }
echo.
echo     function nextSlide(^) {
echo         currentSlide = (currentSlide + 1^) %% slides.length;
echo         showSlide(currentSlide^);
echo     }
echo.
echo     // Auto slide
echo     if (slides.length ^> 1^) {
echo         setInterval(nextSlide, 5000^);
echo     }
echo.
echo     // Dot navigation
echo     dots.forEach((dot, index^) =^> {
echo         dot.addEventListener('click', (^) =^> {
echo             currentSlide = index;
echo             showSlide(currentSlide^);
echo         }^);
echo     }^);
echo }
echo.
echo function initializeMobileMenu(^) {
echo     const mobileMenuButton = document.getElementById('mobile-menu-button'^);
echo     const mobileMenu = document.getElementById('mobile-menu'^);
echo.
echo     if (mobileMenuButton ^&^& mobileMenu^) {
echo         mobileMenuButton.addEventListener('click', function(^) {
echo             mobileMenu.classList.toggle('hidden'^);
echo         }^);
echo     }
echo }
echo.
echo function initializeAnimations(^) {
echo     // Intersection Observer for scroll animations
echo     const observer = new IntersectionObserver((entries^) =^> {
echo         entries.forEach(entry =^> {
echo             if (entry.isIntersecting^) {
echo                 entry.target.classList.add('visible'^);
echo                 
echo                 // Counter animation
echo                 if (entry.target.classList.contains('counter'^)^) {
echo                     const target = parseInt(entry.target.dataset.target^);
echo                     animateCounter(entry.target, target^);
echo                     observer.unobserve(entry.target^);
echo                 }
echo             }
echo         }^);
echo     }^);
echo.
echo     // Observe elements
echo     document.querySelectorAll('.fade-in-on-scroll'^).forEach(el =^> {
echo         observer.observe(el^);
echo     }^);
echo     
echo     document.querySelectorAll('.counter'^).forEach(counter =^> {
echo         observer.observe(counter^);
echo     }^);
echo }
echo.
echo function animateCounter(element, target^) {
echo     let current = 0;
echo     const increment = target / 50;
echo     const timer = setInterval((^) =^> {
echo         current += increment;
echo         if (current ^>= target^) {
echo             current = target;
echo             clearInterval(timer^);
echo         }
echo         element.textContent = Math.floor(current^) + (target ^> 99 ? '+' : ''^);
echo     }, 40^);
echo }
) > static\js\main.js

:: Cập nhật gitignore
echo 📝 Updating .gitignore...
echo. >> .gitignore
echo # Node.js >> .gitignore
echo node_modules/ >> .gitignore
echo npm-debug.log* >> .gitignore
echo. >> .gitignore
echo # Tailwind generated CSS >> .gitignore
echo static/css/style.css >> .gitignore
echo. >> .gitignore
echo # Package lock files >> .gitignore
echo package-lock.json >> .gitignore

echo.
echo ✅ Setup completed successfully!
echo.
echo 📋 Next steps:
echo 1. Install Node.js from https://nodejs.org/ (if not installed)
echo 2. Run: npm install
echo 3. Run: npm run dev
echo 4. Update your templates to use Tailwind classes
echo.
echo 🚀 Happy coding!
pause