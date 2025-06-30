import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

# Configurar estilo de matplotlib y seaborn
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

class SistemaAnalisisProfesional:
    def __init__(self, root):
        self.root = root
        self.root.title("🔍 Sistema Profesional de Análisis de Datos")
        
        # Obtener dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Configurar ventana para usar toda la pantalla
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.state('zoomed')  # Maximizar la ventana
        self.root.configure(bg='#f0f0f0')
        
        # Configurar estilo
        self.setup_styles()
        
        # Crear DataFrame de ejemplo con más datos
        self.create_sample_data()
        
        # Crear interfaz
        self.create_interface()
        
        # Mostrar gráfico inicial
        self.show_overview()
        
    def setup_styles(self):
        """Configurar estilos personalizados"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar colores personalizados
        style.configure('Header.TLabel', 
                       font=('Arial', 16, 'bold'),
                       foreground='#2c3e50',
                       background='#f0f0f0')
        
        style.configure('Custom.TButton',
                       font=('Arial', 10, 'bold'),
                       foreground='white')
        
        style.map('Custom.TButton',
                 background=[('active', '#3498db'),
                           ('!active', '#34495e')])
        
    def create_sample_data(self):
        """Crear dataset más completo"""
        np.random.seed(42)
        
        amenazas = [
            'Caídas en web/móvil', 'Interrupciones digitales', 
            'Gestión de accesos', 'Falta de comunicación', 
            'Problemas de seguridad', 'Desactualización de sistemas',
            'Vulnerabilidades', 'Errores humanos', 'Fallos de hardware',
            'Pérdida de datos'
        ]
        
        valores = [40, 30, 25, 20, 15, 12, 10, 8, 6, 4]
        impacto = np.random.uniform(1, 10, len(amenazas))
        probabilidad = np.random.uniform(0.1, 0.9, len(amenazas))
        
        self.data = pd.DataFrame({
            'Amenaza': amenazas,
            'Valor': valores,
            'Impacto': impacto,
            'Probabilidad': probabilidad,
            'Riesgo': np.array(valores) * impacto * probabilidad,
            'Porcentaje': (np.array(valores) / sum(valores) * 100)
        })
        
        # Calcular valores acumulados
        self.data['Valor_Acumulado'] = self.data['Valor'].cumsum()
        self.data['Porcentaje_Acumulado'] = self.data['Porcentaje'].cumsum()
        
    def load_cybersecurity_data(self, filepath="Global_Cybersecurity_Threats_2015-2024.csv"):
        """Cargar el dataset de ciberseguridad."""
        try:
            self.cybersecurity_data = pd.read_csv(filepath)
            print(f"Dataset {filepath} cargado exitosamente.")
            print(f"Columnas: {self.cybersecurity_data.columns.tolist()}")
            print(f"Primeras 5 filas:\n{self.cybersecurity_data.head()}")
        except FileNotFoundError:
            messagebox.showerror("Error de archivo", f"No se encontró el archivo: {filepath}")
            self.cybersecurity_data = None
        except Exception as e:
            messagebox.showerror("Error de carga", f"Error al cargar {filepath}: {e}")
            self.cybersecurity_data = None

    def create_interface(self):
        """Crear la interfaz principal"""
        # Frame principal con scroll
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_container)
        
        # Panel de control
        self.create_control_panel(main_container)
        
        # Área de visualización
        self.create_visualization_area(main_container)
        
        # Panel de información
        self.create_info_panel(main_container)
        
    def create_header(self, parent):
        """Crear header de la aplicación"""
        header_frame = ttk.Frame(parent)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(header_frame, 
                               text="📊 Sistema de Análisis Estadístico Avanzado",
                               style='Header.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(header_frame,
                                  text="Análisis integral de amenazas y riesgos empresariales",
                                  font=('Arial', 10, 'italic'),
                                  foreground='#7f8c8d')
        subtitle_label.pack()
        
    def create_control_panel(self, parent):
        """Crear panel de control con botones organizados"""
        control_frame = ttk.LabelFrame(parent, text="🎛️ Panel de Control", padding=15)
        control_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Organizar botones en categorías
        categories = [
            ("Estadísticas Básicas", [
                ("📉 Mínimos", self.show_min, "#e74c3c"),
                ("📈 Máximos", self.show_max, "#27ae60"),
                ("📊 Rango", self.show_range, "#f39c12"),
                ("⚖️ Media", self.show_mean, "#3498db")
            ]),
            ("Medidas de Posición", [
                ("🎯 Mediana", self.show_median, "#9b59b6"),
                ("📐 Cuartiles", self.show_quartiles, "#1abc9c"),
                ("📋 Percentiles", self.show_percentiles, "#34495e")
            ]),
            ("Medidas de Dispersión", [
                ("📏 Varianza", self.show_variance, "#e67e22"),
                ("📐 Desv. Estándar", self.show_std, "#c0392b"),
                ("📊 Coef. Variación", self.show_cv, "#8e44ad")
            ]),
            ("Análisis Avanzado", [
                ("🔍 Correlación", self.show_correlation, "#2c3e50"),
                ("📈 Pareto", self.show_pareto, "#16a085"),
                ("🎭 Distribución", self.show_distribution, "#d35400")
            ])
        ]
        
        for i, (category_name, buttons) in enumerate(categories):
            category_frame = ttk.LabelFrame(control_frame, text=category_name, padding=10)
            category_frame.grid(row=i//2, column=i%2, padx=10, pady=5, sticky='ew')
            
            for j, (text, command, color) in enumerate(buttons):
                btn = ttk.Button(category_frame, text=text, command=command,
                               style='Custom.TButton', width=18)
                btn.grid(row=j//2, column=j%2, padx=5, pady=3, sticky='ew')
        
        # Configurar peso de columnas
        control_frame.columnconfigure(0, weight=1)
        control_frame.columnconfigure(1, weight=1)
        
    def create_visualization_area(self, parent):
        """Crear área de visualización"""
        viz_frame = ttk.LabelFrame(parent, text="📈 Visualización de Datos", padding=15)
        viz_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Crear notebook para múltiples gráficos
        self.notebook = ttk.Notebook(viz_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Tab principal
        self.main_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.main_tab, text="📊 Gráfico Principal")
        
        # Tab de comparación
        self.comparison_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.comparison_tab, text="🔄 Comparación")

        # Nueva pestaña para análisis de Ciberseguridad
        self.cybersecurity_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.cybersecurity_tab, text="🛡️ Ciberseguridad")
        
    def create_info_panel(self, parent):
        """Crear panel de información estadística"""
        info_frame = ttk.LabelFrame(parent, text="ℹ️ Información Estadística", padding=15)
        info_frame.pack(fill=tk.X)
        
        # Text widget para mostrar estadísticas
        self.info_text = tk.Text(info_frame, height=8, wrap=tk.WORD,
                                font=('Consolas', 10), bg='#f8f9fa',
                                fg='#2c3e50', relief='flat')
        
        scrollbar = ttk.Scrollbar(info_frame, orient="vertical", command=self.info_text.yview)
        self.info_text.configure(yscrollcommand=scrollbar.set)
        
        self.info_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def clear_plot_area(self, tab_frame):
        """Limpiar área de gráfico"""
        for widget in tab_frame.winfo_children():
            widget.destroy()
    
    def create_plot_canvas(self, fig, tab_frame):
        """Crear canvas para el gráfico"""
        canvas = FigureCanvasTkAgg(fig, master=tab_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Añadir toolbar
        toolbar_frame = ttk.Frame(tab_frame)
        toolbar_frame.pack(fill=tk.X)
        
        from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
        toolbar.update()
        
    def update_info_panel(self, title, stats_dict):
        """Actualizar panel de información"""
        self.info_text.delete(1.0, tk.END)
        
        info = f"{'='*50}\n"
        info += f"🔍 ANÁLISIS: {title.upper()}\n"
        info += f"{'='*50}\n\n"
        
        for key, value in stats_dict.items():
            if isinstance(value, (int, float)):
                info += f"• {key}: {value:.4f}\n"
            else:
                info += f"• {key}: {value}\n"
        
        info += f"\n{'='*50}\n"
        info += f"📊 Total de registros: {len(self.data)}\n"
        info += f"🎯 Fecha de análisis: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        
        self.info_text.insert(1.0, info)
    
    def show_overview(self):
        """Mostrar vista general"""
        self.clear_plot_area(self.main_tab)
        
        # Obtener dimensiones del área de visualización
        width = self.main_tab.winfo_width()
        height = self.main_tab.winfo_height()
        
        # Ajustar tamaño de la figura según el espacio disponible
        fig_width = max(14, width / 100)  # Convertir píxeles a pulgadas
        fig_height = max(10, height / 100)
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(fig_width, fig_height))
        fig.suptitle('📊 Vista General del Análisis de Amenazas', fontsize=16, fontweight='bold', y=0.95)
        
        # Gráfico de barras principal
        colors = plt.cm.Set3(np.linspace(0, 1, len(self.data)))
        bars = ax1.bar(range(len(self.data)), self.data['Valor'], color=colors)
        ax1.set_title('💼 Valores de Amenazas', fontweight='bold', pad=20)
        ax1.set_xlabel('Amenazas')
        ax1.set_ylabel('Valor')
        ax1.set_xticks(range(len(self.data)))
        ax1.set_xticklabels([a[:15] + '...' if len(a) > 15 else a for a in self.data['Amenaza']], 
                           rotation=45, ha='right')
        
        # Añadir valores en las barras
        for bar, value in zip(bars, self.data['Valor']):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                    f'{value}', ha='center', va='bottom', fontweight='bold')
        
        # Gráfico circular
        ax2.pie(self.data['Valor'], labels=self.data['Amenaza'], autopct='%1.1f%%',
                startangle=90, colors=colors)
        ax2.set_title('🎯 Distribución Porcentual', fontweight='bold', pad=20)
        
        # Gráfico de dispersión
        scatter = ax3.scatter(self.data['Impacto'], self.data['Probabilidad'], 
                             s=self.data['Valor']*10, c=self.data['Riesgo'], 
                             cmap='viridis', alpha=0.7)
        ax3.set_title('⚠️ Matriz de Riesgo', fontweight='bold', pad=20)
        ax3.set_xlabel('Impacto')
        ax3.set_ylabel('Probabilidad')
        plt.colorbar(scatter, ax=ax3, label='Nivel de Riesgo')
        
        # Histograma
        ax4.hist(self.data['Valor'], bins=8, color='skyblue', alpha=0.7, edgecolor='black')
        ax4.set_title('📈 Distribución de Valores', fontweight='bold', pad=20)
        ax4.set_xlabel('Rangos de Valor')
        ax4.set_ylabel('Frecuencia')
        
        plt.tight_layout(pad=3.0)
        self.create_plot_canvas(fig, self.main_tab)
        
        # Actualizar panel de información
        stats = {
            'Total de amenazas': len(self.data),
            'Valor promedio': self.data['Valor'].mean(),
            'Riesgo máximo': self.data['Riesgo'].max(),
            'Amenaza crítica': self.data.loc[self.data['Riesgo'].idxmax(), 'Amenaza']
        }
        self.update_info_panel("Vista General", stats)
    
    def show_min(self):
        """Mostrar análisis de valores mínimos"""
        self.clear_plot_area(self.main_tab)
        
        numeric_cols = ['Valor', 'Impacto', 'Probabilidad', 'Riesgo']
        min_values = self.data[numeric_cols].min()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle('📉 Análisis de Valores Mínimos', fontsize=16, fontweight='bold')
        
        # Gráfico de barras de mínimos
        colors = ['#e74c3c', '#3498db', '#f39c12', '#27ae60']
        bars = ax1.bar(numeric_cols, min_values, color=colors, alpha=0.8)
        ax1.set_title('📊 Valores Mínimos por Categoría')
        ax1.set_ylabel('Valor Mínimo')
        
        for bar, value in zip(bars, min_values):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                    f'{value:.2f}', ha='center', va='bottom', fontweight='bold')
        
        # Identificar registros con valores mínimos
        min_records = []
        for col in numeric_cols:
            min_idx = self.data[col].idxmin()
            min_records.append(self.data.loc[min_idx, 'Amenaza'])
        
        # Gráfico de identificación
        y_pos = np.arange(len(numeric_cols))
        ax2.barh(y_pos, min_values, color=colors, alpha=0.8)
        ax2.set_yticks(y_pos)
        ax2.set_yticklabels(numeric_cols)
        ax2.set_title('🎯 Amenazas con Valores Mínimos')
        ax2.set_xlabel('Valor')
        
        plt.tight_layout()
        self.create_plot_canvas(fig, self.main_tab)
        
        stats = {f'Mínimo {col}': min_values[col] for col in numeric_cols}
        for i, col in enumerate(numeric_cols):
            stats[f'Amenaza mín. {col}'] = min_records[i]
        self.update_info_panel("Valores Mínimos", stats)
    
    def show_max(self):
        """Mostrar análisis de valores máximos"""
        self.clear_plot_area(self.main_tab)
        
        numeric_cols = ['Valor', 'Impacto', 'Probabilidad', 'Riesgo']
        max_values = self.data[numeric_cols].max()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle('📈 Análisis de Valores Máximos', fontsize=16, fontweight='bold')
        
        # Gráfico de barras de máximos
        colors = ['#27ae60', '#e74c3c', '#9b59b6', '#f39c12']
        bars = ax1.bar(numeric_cols, max_values, color=colors, alpha=0.8)
        ax1.set_title('📊 Valores Máximos por Categoría')
        ax1.set_ylabel('Valor Máximo')
        
        for bar, value in zip(bars, max_values):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max_values.max()*0.02,
                    f'{value:.2f}', ha='center', va='bottom', fontweight='bold')
        
        # Radar chart para valores máximos
        angles = np.linspace(0, 2*np.pi, len(numeric_cols), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))
        
        max_normalized = max_values / max_values.max()
        values = np.concatenate((max_normalized, [max_normalized[0]]))
        
        ax2 = plt.subplot(122, projection='polar')
        ax2.plot(angles, values, 'o-', linewidth=2, color='#27ae60')
        ax2.fill(angles, values, alpha=0.25, color='#27ae60')
        ax2.set_xticks(angles[:-1])
        ax2.set_xticklabels(numeric_cols)
        ax2.set_title('🎯 Perfil de Máximos (Normalizado)', y=1.08)
        
        plt.tight_layout()
        self.create_plot_canvas(fig, self.main_tab)
        
        stats = {f'Máximo {col}': max_values[col] for col in numeric_cols}
        self.update_info_panel("Valores Máximos", stats)
    
    def show_range(self):
        """Mostrar análisis de rangos"""
        self.clear_plot_area(self.main_tab)
        
        numeric_cols = ['Valor', 'Impacto', 'Probabilidad', 'Riesgo']
        ranges = self.data[numeric_cols].max() - self.data[numeric_cols].min()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle('📊 Análisis de Rangos', fontsize=16, fontweight='bold')
        
        # Gráfico de rangos
        colors = plt.cm.viridis(np.linspace(0, 1, len(numeric_cols)))
        bars = ax1.bar(numeric_cols, ranges, color=colors, alpha=0.8)
        ax1.set_title('📏 Rango por Variable')
        ax1.set_ylabel('Rango (Máx - Mín)')
        
        for bar, value in zip(bars, ranges):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + ranges.max()*0.02,
                    f'{value:.2f}', ha='center', va='bottom', fontweight='bold')
        
        # Box plot para mostrar dispersión
        box_data = [self.data[col] for col in numeric_cols]
        bp = ax2.boxplot(box_data, labels=numeric_cols, patch_artist=True)
        
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        
        ax2.set_title('📦 Distribución y Dispersión')
        ax2.set_ylabel('Valores')
        
        plt.tight_layout()
        self.create_plot_canvas(fig, self.main_tab)
        
        stats = {f'Rango {col}': ranges[col] for col in numeric_cols}
        stats['Coef. Variación Promedio'] = (self.data[numeric_cols].std() / self.data[numeric_cols].mean()).mean()
        self.update_info_panel("Análisis de Rangos", stats)
    
    def show_mean(self):
        """Mostrar análisis de medias"""
        self.clear_plot_area(self.main_tab)
        
        numeric_cols = ['Valor', 'Impacto', 'Probabilidad', 'Riesgo']
        means = self.data[numeric_cols].mean()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle('⚖️ Análisis de Medias', fontsize=16, fontweight='bold')
        
        # Gráfico de medias vs valores individuales
        x_pos = np.arange(len(self.data))
        ax1.scatter(x_pos, self.data['Valor'], alpha=0.6, s=60, color='lightblue', label='Valores individuales')
        ax1.axhline(y=means['Valor'], color='red', linestyle='--', linewidth=2, label=f'Media = {means["Valor"]:.2f}')
        ax1.fill_between(x_pos, means['Valor'] - self.data['Valor'].std(), 
                        means['Valor'] + self.data['Valor'].std(), 
                        alpha=0.2, color='red', label='±1 Desviación Estándar')
        ax1.set_title('📊 Valores vs Media')
        ax1.set_xlabel('Índice de Amenaza')
        ax1.set_ylabel('Valor')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Comparación de medias
        colors = ['#3498db', '#e74c3c', '#f39c12', '#27ae60']
        bars = ax2.bar(numeric_cols, means, color=colors, alpha=0.8)
        ax2.set_title('📈 Comparación de Medias')
        ax2.set_ylabel('Valor Promedio')
        
        for bar, value in zip(bars, means):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + means.max()*0.02,
                    f'{value:.2f}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        self.create_plot_canvas(fig, self.main_tab)
        
        stats = {f'Media {col}': means[col] for col in numeric_cols}
        stats['Media Harmónica (Valor)'] = len(self.data['Valor']) / (1/self.data['Valor']).sum()
        stats['Media Geométrica (Valor)'] = np.power(self.data['Valor'].prod(), 1/len(self.data['Valor']))
        self.update_info_panel("Análisis de Medias", stats)
    
    def show_median(self):
        """Mostrar análisis de medianas"""
        self.clear_plot_area(self.main_tab)
        
        numeric_cols = ['Valor', 'Impacto', 'Probabilidad', 'Riesgo']
        medians = self.data[numeric_cols].median()
        means = self.data[numeric_cols].mean()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle('🎯 Análisis de Medianas', fontsize=16, fontweight='bold')
        
        # Comparación Media vs Mediana
        x = np.arange(len(numeric_cols))
        width = 0.35
        
        bars1 = ax1.bar(x - width/2, means, width, label='Media', color='skyblue', alpha=0.8)
        bars2 = ax1.bar(x + width/2, medians, width, label='Mediana', color='lightcoral', alpha=0.8)
        
        ax1.set_title('⚖️ Media vs Mediana')
        ax1.set_ylabel('Valor')
        ax1.set_xticks(x)
        ax1.set_xticklabels(numeric_cols)
        ax1.legend()
        
        # Añadir valores en las barras
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax1.text(bar.get_x() + bar.get_width()/2., height + max(means.max(), medians.max())*0.01,
                        f'{height:.2f}', ha='center', va='bottom', fontsize=9)
        
        # Violin plot para mostrar distribución
        violin_data = [self.data[col] for col in numeric_cols]
        parts = ax2.violinplot(violin_data, positions=range(len(numeric_cols)), showmeans=True, showmedians=True)
        
        ax2.set_title('🎻 Distribución de Datos')
        ax2.set_ylabel('Valor')
        ax2.set_xticks(range(len(numeric_cols)))
        ax2.set_xticklabels(numeric_cols)
        
        # Colorear los violines
        colors = ['#3498db', '#e74c3c', '#f39c12', '#27ae60']
        for pc, color in zip(parts['bodies'], colors):
            pc.set_facecolor(color)
            pc.set_alpha(0.7)
        
        plt.tight_layout()
        self.create_plot_canvas(fig, self.main_tab)
        
        stats = {f'Mediana {col}': medians[col] for col in numeric_cols}
        stats.update({f'Diferencia Media-Mediana {col}': abs(means[col] - medians[col]) for col in numeric_cols})
        self.update_info_panel("Análisis de Medianas", stats)
    
    def show_quartiles(self):
        """Mostrar análisis de cuartiles"""
        self.clear_plot_area(self.main_tab)
        
        numeric_cols = ['Valor', 'Impacto', 'Probabilidad', 'Riesgo']
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('📐 Análisis de Cuartiles', fontsize=16, fontweight='bold')
        
        # Box plot detallado
        bp = ax1.boxplot([self.data[col] for col in numeric_cols], 
                        labels=numeric_cols, patch_artist=True, showfliers=True)
        
        colors = ['#3498db', '#e74c3c', '#f39c12', '#27ae60']
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        
        ax1.set_title('📦 Box Plot con Cuartiles')
        ax1.set_ylabel('Valores')
        ax1.grid(True, alpha=0.3)
        
        # Cuartiles para la variable principal (Valor)
        q1, q2, q3 = self.data['Valor'].quantile([0.25, 0.5, 0.75])
        
        ax2.hist(self.data['Valor'], bins=10, alpha=0.7, color='skyblue', edgecolor='black')
        ax2.axvline(q1, color='red', linestyle='--', label=f'Q1 = {q1:.2f}')
        ax2.axvline(q2, color='green', linestyle='--', label=f'Q2 = {q2:.2f}')
        ax2.axvline(q3, color='blue', linestyle='--', label=f'Q3 = {q3:.2f}')
        ax2.set_title('📊 Distribución con Cuartiles (Valor)')
        ax2.set_xlabel('Valor')
        ax2.set_ylabel('Frecuencia')
        ax2.legend()
        
        # Tabla de cuartiles
        quartile_data = []
        for col in numeric_cols:
            q_values = self.data[col].quantile([0.25, 0.5, 0.75])
            quartile_data.append(q_values.values)
        
        im = ax3.imshow(quartile_data, cmap='RdYlBu', aspect='auto')
        ax3.set_xticks(range(3))
        ax3.set_xticklabels(['Q1', 'Q2', 'Q3'])
        ax3.set_yticks(range(len(numeric_cols)))
        ax3.set_yticklabels(numeric_cols)
        ax3.set_title('🔥 Mapa de Calor de Cuartiles')
        
        # Añadir valores en el mapa de calor
        for i in range(len(numeric_cols)):
            for j in range(3):
                ax3.text(j, i, f'{quartile_data[i][j]:.2f}', 
                        ha='center', va='center', fontweight='bold', color='white')
        
        plt.colorbar(im, ax=ax3, label='Valor')
        
        # Rango intercuartílico
        iqr_values = []
        for col in numeric_cols:
            q1, q3 = self.data[col].quantile([0.25, 0.75])
            iqr_values.append(q3 - q1)
        
        bars = ax4.bar(numeric_cols, iqr_values, color=colors, alpha=0.8)
        ax4.set_title('📏 Rango Intercuartílico (IQR)')
        ax4.set_ylabel('IQR')
        
        for bar, value in zip(bars, iqr_values):
            ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(iqr_values)*0.02,
                    f'{value:.2f}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        self.create_plot_canvas(fig, self.main_tab)
        
        stats = {}
        for col in numeric_cols:
            q1, q2, q3 = self.data[col].quantile([0.25, 0.5, 0.75])
            stats[f'Q1 {col}'] = q1
            stats[f'Q2 {col}'] = q2
            stats[f'Q3 {col}'] = q3
            stats[f'IQR {col}'] = q3 - q1
        
        self.update_info_panel("Análisis de Cuartiles", stats)
    
    def show_percentiles(self):
        """Mostrar análisis de percentiles"""
        self.clear_plot_area(self.main_tab)
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('📋 Análisis de Percentiles', fontsize=16, fontweight='bold')
        
        # Percentiles para la variable Valor
        percentiles = [10, 25, 50, 75, 90, 95, 99]
        perc_values = [self.data['Valor'].quantile(p/100) for p in percentiles]
        
        ax1.plot(percentiles, perc_values, 'o-', linewidth=2, markersize=8, color='#3498db')
        ax1.fill_between(percentiles, perc_values, alpha=0.3, color='#3498db')
        ax1.set_title('📈 Curva de Percentiles (Valor)')
        ax1.set_xlabel('Percentil')
        ax1.set_ylabel('Valor')
        ax1.grid(True, alpha=0.3)
        
        # Añadir etiquetas de valor
        for p, v in zip(percentiles, perc_values):
            ax1.annotate(f'{v:.1f}', (p, v), textcoords="offset points", 
                        xytext=(0,10), ha='center', fontsize=9)
        
        # Distribución acumulativa
        sorted_values = np.sort(self.data['Valor'])
        y_values = np.arange(1, len(sorted_values) + 1) / len(sorted_values) * 100
        
        ax2.plot(sorted_values, y_values, linewidth=2, color='#e74c3c')
        ax2.fill_between(sorted_values, y_values, alpha=0.3, color='#e74c3c')
        ax2.set_title('📊 Función de Distribución Acumulativa')
        ax2.set_xlabel('Valor')
        ax2.set_ylabel('Percentil')
        ax2.grid(True, alpha=0.3)
        
        # Comparación de percentiles entre variables
        perc_25_75 = {}
        for col in ['Valor', 'Impacto', 'Probabilidad', 'Riesgo']:
            perc_25_75[col] = [self.data[col].quantile(0.25), self.data[col].quantile(0.75)]
        
        x_labels = list(perc_25_75.keys())
        p25_values = [perc_25_75[col][0] for col in x_labels]
        p75_values = [perc_25_75[col][1] for col in x_labels]
        
        x = np.arange(len(x_labels))
        width = 0.35
        
        bars1 = ax3.bar(x - width/2, p25_values, width, label='Percentil 25', 
                       color='lightblue', alpha=0.8)
        bars2 = ax3.bar(x + width/2, p75_values, width, label='Percentil 75', 
                       color='darkblue', alpha=0.8)
        
        ax3.set_title('🔄 Comparación P25 vs P75')
        ax3.set_ylabel('Valor')
        ax3.set_xticks(x)
        ax3.set_xticklabels(x_labels)
        ax3.legend()
        
        # Identificar outliers usando IQR
        outliers_data = []
        for col in ['Valor', 'Impacto', 'Probabilidad', 'Riesgo']:
            q1, q3 = self.data[col].quantile([0.25, 0.75])
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outliers = self.data[(self.data[col] < lower_bound) | (self.data[col] > upper_bound)]
            outliers_data.append(len(outliers))
        
        colors = ['#3498db', '#e74c3c', '#f39c12', '#27ae60']
        bars = ax4.bar(['Valor', 'Impacto', 'Probabilidad', 'Riesgo'], 
                      outliers_data, color=colors, alpha=0.8)
        ax4.set_title('🚨 Detección de Outliers')
        ax4.set_ylabel('Número de Outliers')
        
        for bar, value in zip(bars, outliers_data):
            ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                    f'{value}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        self.create_plot_canvas(fig, self.main_tab)
        
        stats = {}
        for p in [5, 10, 25, 50, 75, 90, 95]:
            stats[f'P{p} (Valor)'] = self.data['Valor'].quantile(p/100)
        stats['Total Outliers'] = sum(outliers_data)
        
        self.update_info_panel("Análisis de Percentiles", stats)
    
    def show_variance(self):
        """Mostrar análisis de varianza"""
        self.clear_plot_area(self.main_tab)
        
        numeric_cols = ['Valor', 'Impacto', 'Probabilidad', 'Riesgo']
        variances = self.data[numeric_cols].var()
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('📏 Análisis de Varianza', fontsize=16, fontweight='bold')
        
        # Gráfico de varianzas
        colors = ['#e67e22', '#3498db', '#e74c3c', '#27ae60']
        bars = ax1.bar(numeric_cols, variances, color=colors, alpha=0.8)
        ax1.set_title('📊 Varianza por Variable')
        ax1.set_ylabel('Varianza')
        
        for bar, value in zip(bars, variances):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + variances.max()*0.02,
                    f'{value:.2f}', ha='center', va='bottom', fontweight='bold')
        
        # Descomposición de varianza para Valor
        mean_val = self.data['Valor'].mean()
        squared_deviations = (self.data['Valor'] - mean_val) ** 2
        
        ax2.scatter(range(len(self.data)), self.data['Valor'], 
                   s=squared_deviations*5, alpha=0.6, color='orange', 
                   label='Valores (tamaño = desviación²)')
        ax2.axhline(y=mean_val, color='red', linestyle='--', linewidth=2, 
                   label=f'Media = {mean_val:.2f}')
        ax2.set_title('🎯 Visualización de Varianza (Valor)')
        ax2.set_xlabel('Índice')
        ax2.set_ylabel('Valor')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Mapa de calor de correlaciones (relacionado con varianza)
        corr_matrix = self.data[numeric_cols].corr()
        im = ax3.imshow(corr_matrix, cmap='RdBu', vmin=-1, vmax=1)
        ax3.set_xticks(range(len(numeric_cols)))
        ax3.set_yticks(range(len(numeric_cols)))
        ax3.set_xticklabels(numeric_cols)
        ax3.set_yticklabels(numeric_cols)
        ax3.set_title('🔥 Matriz de Correlación')
        
        # Añadir valores de correlación
        for i in range(len(numeric_cols)):
            for j in range(len(numeric_cols)):
                ax3.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                        ha='center', va='center', fontweight='bold',
                        color='white' if abs(corr_matrix.iloc[i, j]) > 0.5 else 'black')
        
        plt.colorbar(im, ax=ax3, label='Correlación')
        
        # Análisis de contribución a la varianza total
        total_variance = variances.sum()
        var_contribution = (variances / total_variance) * 100
        
        wedges, texts, autotexts = ax4.pie(var_contribution, labels=numeric_cols, 
                                          autopct='%1.1f%%', startangle=90, 
                                          colors=colors)
        ax4.set_title('🥧 Contribución a la Varianza Total')
        
        plt.tight_layout()
        self.create_plot_canvas(fig, self.main_tab)
        
        stats = {f'Varianza {col}': variances[col] for col in numeric_cols}
        stats['Varianza Total'] = total_variance
        stats['Coef. Variación Medio'] = (self.data[numeric_cols].std() / self.data[numeric_cols].mean()).mean()
        
        self.update_info_panel("Análisis de Varianza", stats)
    
    def show_std(self):
        """Mostrar análisis de desviación estándar"""
        self.clear_plot_area(self.main_tab)
        
        numeric_cols = ['Valor', 'Impacto', 'Probabilidad', 'Riesgo']
        std_devs = self.data[numeric_cols].std()
        means = self.data[numeric_cols].mean()
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('📐 Análisis de Desviación Estándar', fontsize=16, fontweight='bold')
        
        # Gráfico de desviaciones estándar
        colors = ['#c0392b', '#3498db', '#e74c3c', '#27ae60']
        bars = ax1.bar(numeric_cols, std_devs, color=colors, alpha=0.8)
        ax1.set_title('📊 Desviación Estándar por Variable')
        ax1.set_ylabel('Desviación Estándar')
        
        for bar, value in zip(bars, std_devs):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + std_devs.max()*0.02,
                    f'{value:.2f}', ha='center', va='bottom', fontweight='bold')
        
        # Bandas de confianza para Valor
        x_vals = range(len(self.data))
        mean_val = means['Valor']
        std_val = std_devs['Valor']
        
        ax2.plot(x_vals, self.data['Valor'], 'o-', color='blue', alpha=0.7, label='Valores')
        ax2.axhline(y=mean_val, color='red', linestyle='-', linewidth=2, label=f'Media = {mean_val:.2f}')
        ax2.fill_between(x_vals, mean_val - std_val, mean_val + std_val, 
                        alpha=0.2, color='red', label='±1σ')
        ax2.fill_between(x_vals, mean_val - 2*std_val, mean_val + 2*std_val, 
                        alpha=0.1, color='orange', label='±2σ')
        ax2.set_title('📈 Bandas de Confianza (Valor)')
        ax2.set_xlabel('Índice')
        ax2.set_ylabel('Valor')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Coeficiente de variación
        cv_values = (std_devs / means) * 100
        bars = ax3.bar(numeric_cols, cv_values, color=colors, alpha=0.8)
        ax3.set_title('📊 Coeficiente de Variación (%)')
        ax3.set_ylabel('CV (%)')
        
        for bar, value in zip(bars, cv_values):
            ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + cv_values.max()*0.02,
                    f'{value:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        # Distribución normal comparativa
        x_norm = np.linspace(self.data['Valor'].min(), self.data['Valor'].max(), 100)
        y_norm = (1/(std_val * np.sqrt(2*np.pi))) * np.exp(-0.5*((x_norm - mean_val)/std_val)**2)
        
        ax4.hist(self.data['Valor'], bins=8, density=True, alpha=0.7, 
                color='skyblue', edgecolor='black', label='Datos reales')
        ax4.plot(x_norm, y_norm, 'r-', linewidth=2, label='Distribución Normal')
        ax4.set_title('📊 Comparación con Distribución Normal')
        ax4.set_xlabel('Valor')
        ax4.set_ylabel('Densidad')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        self.create_plot_canvas(fig, self.main_tab)
        
        stats = {f'Desv. Estándar {col}': std_devs[col] for col in numeric_cols}
        stats.update({f'Coef. Variación {col}': cv_values[col] for col in numeric_cols})
        
        self.update_info_panel("Análisis de Desviación Estándar", stats)
    
    def show_cv(self):
        """Mostrar análisis de coeficiente de variación"""
        self.clear_plot_area(self.main_tab)
        
        numeric_cols = ['Valor', 'Impacto', 'Probabilidad', 'Riesgo']
        means = self.data[numeric_cols].mean()
        std_devs = self.data[numeric_cols].std()
        cv_values = (std_devs / means) * 100
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle('📊 Análisis de Coeficiente de Variación', fontsize=16, fontweight='bold')
        
        # Gráfico de coeficientes de variación
        colors = ['#8e44ad', '#3498db', '#e74c3c', '#27ae60']
        bars = ax1.bar(numeric_cols, cv_values, color=colors, alpha=0.8)
        ax1.set_title('📊 Coeficiente de Variación por Variable')
        ax1.set_ylabel('CV (%)')
        
        # Añadir líneas de referencia
        ax1.axhline(y=15, color='green', linestyle='--', alpha=0.7, label='Baja variabilidad (<15%)')
        ax1.axhline(y=30, color='orange', linestyle='--', alpha=0.7, label='Variabilidad moderada (15-30%)')
        ax1.axhline(y=30, color='red', linestyle='--', alpha=0.7, label='Alta variabilidad (>30%)')
        
        for bar, value in zip(bars, cv_values):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + cv_values.max()*0.02,
                    f'{value:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Scatter plot: Media vs Desviación Estándar
        scatter = ax2.scatter(means, std_devs, s=cv_values*10, c=cv_values, 
                             cmap='viridis', alpha=0.7, edgecolors='black')
        
        for i, col in enumerate(numeric_cols):
            ax2.annotate(col, (means[col], std_devs[col]), 
                        xytext=(5, 5), textcoords='offset points',
                        fontsize=10, fontweight='bold')
        
        ax2.set_title('🎯 Media vs Desviación Estándar\n(Tamaño = CV)')
        ax2.set_xlabel('Media')
        ax2.set_ylabel('Desviación Estándar')
        ax2.grid(True, alpha=0.3)
        
        plt.colorbar(scatter, ax=ax2, label='Coeficiente de Variación (%)')
        
        plt.tight_layout()
        self.create_plot_canvas(fig, self.main_tab)
        
        # Interpretación del CV
        interpretation = {}
        for col in numeric_cols:
            cv = cv_values[col]
            if cv < 15:
                interpretation[f'Interpretación {col}'] = "Baja variabilidad"
            elif cv < 30:
                interpretation[f'Interpretación {col}'] = "Variabilidad moderada"
            else:
                interpretation[f'Interpretación {col}'] = "Alta variabilidad"
        
        stats = {f'CV {col}': cv_values[col] for col in numeric_cols}
        stats.update(interpretation)
        
        self.update_info_panel("Coeficiente de Variación", stats)
    
    def show_correlation(self):
        """Mostrar análisis de correlación"""
        self.clear_plot_area(self.main_tab)
        
        # Obtener dimensiones del área de visualización
        width = self.main_tab.winfo_width()
        height = self.main_tab.winfo_height()
        
        # Ajustar tamaño de la figura según el espacio disponible
        fig_width = max(14, width / 100)
        fig_height = max(10, height / 100)
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(fig_width, fig_height))
        fig.suptitle('🔍 Análisis de Correlación', fontsize=16, fontweight='bold', y=0.95)
        
        # Mapa de calor de correlación
        corr_matrix = self.data[['Valor', 'Impacto', 'Probabilidad', 'Riesgo']].corr()
        im = ax1.imshow(corr_matrix, cmap='RdBu', vmin=-1, vmax=1)
        ax1.set_xticks(range(len(corr_matrix.columns)))
        ax1.set_yticks(range(len(corr_matrix.columns)))
        ax1.set_xticklabels(corr_matrix.columns)
        ax1.set_yticklabels(corr_matrix.columns)
        ax1.set_title('🔥 Matriz de Correlación', fontweight='bold', pad=20)
        
        # Añadir valores de correlación
        for i in range(len(corr_matrix.columns)):
            for j in range(len(corr_matrix.columns)):
                ax1.text(j, i, f'{corr_matrix.iloc[i, j]:.3f}',
                        ha='center', va='center', fontweight='bold',
                        color='white' if abs(corr_matrix.iloc[i, j]) > 0.5 else 'black')
        
        plt.colorbar(im, ax=ax1, label='Correlación')
        
        # Scatter plot de las correlaciones más fuertes
        col1, col2 = corr_matrix.columns[0], corr_matrix.columns[1]
        correlation_value = corr_matrix.iloc[0, 1]
        
        ax2.scatter(self.data[col1], self.data[col2], alpha=0.7, s=60, color='blue')
        
        # Línea de tendencia
        z = np.polyfit(self.data[col1], self.data[col2], 1)
        p = np.poly1d(z)
        ax2.plot(self.data[col1], p(self.data[col1]), "r--", alpha=0.8, linewidth=2)
        
        ax2.set_title(f'📈 Correlación más fuerte\n{col1} vs {col2} (r={correlation_value:.3f})', 
                     fontweight='bold', pad=20)
        ax2.set_xlabel(col1)
        ax2.set_ylabel(col2)
        ax2.grid(True, alpha=0.3)
        
        # Gráfico de barras de correlaciones
        valor_corr = corr_matrix['Valor'].drop('Valor')
        colors = ['#3498db', '#e74c3c', '#27ae60']
        
        bars = ax3.bar(valor_corr.index, valor_corr.values, color=colors, alpha=0.8)
        ax3.set_title('📊 Correlaciones con "Valor"', fontweight='bold', pad=20)
        ax3.set_ylabel('Correlación')
        ax3.axhline(y=0, color='black', linestyle='-', alpha=0.3)
        ax3.tick_params(axis='x', rotation=45)
        
        for bar, value in zip(bars, valor_corr.values):
            ax3.text(bar.get_x() + bar.get_width()/2, 
                    bar.get_height() + (0.05 if value > 0 else -0.1),
                    f'{value:.3f}', ha='center', va='bottom' if value > 0 else 'top', 
                    fontweight='bold')
        
        # Dendrograma
        from scipy.cluster.hierarchy import dendrogram, linkage
        from scipy.spatial.distance import squareform
        
        distance_matrix = 1 - np.abs(corr_matrix)
        linkage_matrix = linkage(squareform(distance_matrix), method='average')
        
        dendrogram(linkage_matrix, labels=corr_matrix.columns, ax=ax4)
        ax4.set_title('🌳 Dendrograma de Clustering', fontweight='bold', pad=20)
        ax4.set_ylabel('Distancia')
        
        plt.tight_layout(pad=3.0)
        self.create_plot_canvas(fig, self.main_tab)
        
        # Estadísticas de correlación
        stats = {}
        for i, col1 in enumerate(corr_matrix.columns):
            for j, col2 in enumerate(corr_matrix.columns):
                if i < j:  # Evitar duplicados
                    stats[f'Corr {col1}-{col2}'] = corr_matrix.iloc[i, j]
        
        self.update_info_panel("Análisis de Correlación", stats)

    def show_distribution(self):
        """Mostrar análisis de distribución de datos"""
        self.clear_plot_area(self.main_tab)
        
        # Obtener dimensiones del área de visualización
        width = self.main_tab.winfo_width()
        height = self.main_tab.winfo_height()
        
        # Ajustar tamaño de la figura según el espacio disponible
        fig_width = max(14, width / 100)
        fig_height = max(10, height / 100)
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(fig_width, fig_height))
        fig.suptitle('📊 Análisis de Distribución', fontsize=16, fontweight='bold', y=0.95)
        
        # Histograma con curva de densidad
        for i, col in enumerate(['Valor', 'Impacto', 'Probabilidad', 'Riesgo']):
            sns.histplot(data=self.data, x=col, kde=True, ax=ax1, alpha=0.6)
        ax1.set_title('📈 Histogramas con Curvas de Densidad', fontweight='bold', pad=20)
        ax1.set_xlabel('Valor')
        ax1.set_ylabel('Frecuencia')
        ax1.legend(['Valor', 'Impacto', 'Probabilidad', 'Riesgo'], bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # QQ Plot para normalidad
        for i, col in enumerate(['Valor', 'Impacto', 'Probabilidad', 'Riesgo']):
            from scipy import stats
            stats.probplot(self.data[col], dist="norm", plot=ax2)
        ax2.set_title('📊 QQ Plot para Normalidad', fontweight='bold', pad=20)
        ax2.legend(['Valor', 'Impacto', 'Probabilidad', 'Riesgo'], bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # Box plots
        self.data[['Valor', 'Impacto', 'Probabilidad', 'Riesgo']].boxplot(ax=ax3)
        ax3.set_title('📦 Box Plots por Variable', fontweight='bold', pad=20)
        ax3.set_ylabel('Valor')
        ax3.tick_params(axis='x', rotation=45)
        
        # Violin plots
        sns.violinplot(data=self.data[['Valor', 'Impacto', 'Probabilidad', 'Riesgo']], ax=ax4)
        ax4.set_title('🎻 Violin Plots por Variable', fontweight='bold', pad=20)
        ax4.set_ylabel('Valor')
        ax4.tick_params(axis='x', rotation=45)
        
        plt.tight_layout(pad=3.0)
        self.create_plot_canvas(fig, self.main_tab)
        
        # Estadísticas de distribución
        stats = {}
        for col in ['Valor', 'Impacto', 'Probabilidad', 'Riesgo']:
            stats[f'Media {col}'] = self.data[col].mean()
            stats[f'Mediana {col}'] = self.data[col].median()
            stats[f'Moda {col}'] = self.data[col].mode().iloc[0]
            stats[f'Asimetría {col}'] = self.data[col].skew()
            stats[f'Curtosis {col}'] = self.data[col].kurtosis()
        
        self.update_info_panel("Análisis de Distribución", stats)
    
    def show_pareto(self):
        """Mostrar análisis de Pareto"""
        self.clear_plot_area(self.main_tab)
        
        # Obtener dimensiones del área de visualización
        width = self.main_tab.winfo_width()
        height = self.main_tab.winfo_height()
        
        # Ajustar tamaño de la figura según el espacio disponible
        fig_width = max(14, width / 100)
        fig_height = max(6, height / 100)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(fig_width, fig_height))
        fig.suptitle('📈 Análisis de Pareto', fontsize=16, fontweight='bold', y=0.95)
        
        # Ordenar datos por valor descendente
        sorted_data = self.data.sort_values('Valor', ascending=False).reset_index(drop=True)
        
        # Gráfico de Pareto clásico
        cumulative_pct = (sorted_data['Valor'].cumsum() / sorted_data['Valor'].sum()) * 100
        
        # Barras
        colors = plt.cm.Set3(np.linspace(0, 1, len(sorted_data)))
        bars = ax1.bar(range(len(sorted_data)), sorted_data['Valor'], color=colors, alpha=0.8)
        
        # Línea acumulativa
        ax1_twin = ax1.twinx()
        line = ax1_twin.plot(range(len(sorted_data)), cumulative_pct, 'ro-', 
                            linewidth=2, markersize=6, color='red')
        
        # Línea del 80%
        ax1_twin.axhline(y=80, color='orange', linestyle='--', linewidth=2, 
                        alpha=0.8, label='Regla 80/20')
        
        ax1.set_title('📊 Diagrama de Pareto', fontweight='bold', pad=20)
        ax1.set_xlabel('Amenazas (ordenadas por valor)')
        ax1.set_ylabel('Valor', color='blue')
        ax1_twin.set_ylabel('Porcentaje Acumulado', color='red')
        ax1.set_xticks(range(len(sorted_data)))
        ax1.set_xticklabels([name[:10] + '...' if len(name) > 10 else name 
                            for name in sorted_data['Amenaza']], rotation=45, ha='right')
        
        # Identificar el punto del 80%
        pareto_80_idx = np.where(cumulative_pct >= 80)[0]
        if len(pareto_80_idx) > 0:
            first_80_idx = pareto_80_idx[0]
            ax1_twin.annotate(f'80% alcanzado en\nposición {first_80_idx + 1}', 
                             xy=(first_80_idx, 80), xytext=(first_80_idx + 2, 70),
                             arrowprops=dict(arrowstyle='->', color='orange', lw=2),
                             fontsize=10, fontweight='bold', color='orange')
        
        ax1_twin.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # Análisis ABC
        total_value = sorted_data['Valor'].sum()
        category_A = sorted_data[cumulative_pct <= 80]
        category_B = sorted_data[(cumulative_pct > 80) & (cumulative_pct <= 95)]
        category_C = sorted_data[cumulative_pct > 95]
        
        abc_data = {
            'Categoría A (≤80%)': len(category_A),
            'Categoría B (80-95%)': len(category_B),
            'Categoría C (>95%)': len(category_C)
        }
        
        colors_abc = ['#e74c3c', '#f39c12', '#27ae60']
        wedges, texts, autotexts = ax2.pie(abc_data.values(), labels=abc_data.keys(), 
                                          autopct='%1.1f%%', startangle=90, 
                                          colors=colors_abc, explode=(0.05, 0.05, 0.05))
        
        ax2.set_title('🎯 Clasificación ABC', fontweight='bold', pad=20)
        
        # Hacer el texto más legible
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        plt.tight_layout(pad=3.0)
        self.create_plot_canvas(fig, self.main_tab)
        
        # Estadísticas de Pareto
        stats = {
            'Total amenazas': len(sorted_data),
            'Amenazas categoría A': len(category_A),
            'Amenazas categoría B': len(category_B),
            'Amenazas categoría C': len(category_C),
            'Valor acumulado A': category_A['Valor'].sum(),
            'Porcentaje A': (category_A['Valor'].sum() / total_value) * 100,
            'Amenaza más crítica': sorted_data.iloc[0]['Amenaza'],
            'Valor más crítico': sorted_data.iloc[0]['Valor']
        }
        
        self.update_info_panel("Análisis de Pareto", stats)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaAnalisisProfesional(root)
    root.mainloop()