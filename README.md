# 🤖 Robótica Probabilística – Trabalho 3

### 🎓 Alunos:
- Arthur Fellini  
- Michael Lima  
- Pedro Henrique Themoteo  

---

## 📘 Sobre este repositório

Este repositório contém o **Trabalho 3** da disciplina de **Robótica Probabilística**, realizado pelos alunos acima. O objetivo principal é disponibilizar todo o conteúdo desenvolvido em **ROS 2** e **Gazebo** para consulta, aprendizado e compartilhamento.

---

## 📦 Estrutura do Projeto

```
/
├── launch/           # Arquivos de launch ROS 2 para iniciar os nós
├── src/              # Código‑fonte dos nós em Python/C++
├── config/           # Arquivos de configuração (parâmetros, mapas, etc.)
├── worlds/           # Mundo(s) do Gazebo utilizados
├── rviz/             # Configurações do RViz para visualização
├── README.md         # Este arquivo
└── LICENSE           # Licença do projeto (opcional)
```

---

## 🚀 Requisitos

- ROS 2 (dashing / foxy / galactic / humble — conforme versão adotada em sala)  
- Gazebo (versão compatível com ROS 2)  
- Dependências listadas em `package.xml` e `setup.py` de cada pacote

---

## 🛠️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/MichaelLimaDeveloper/Robotica-Probabilistica_Trabalho3.git
   cd Robotica-Probabilistica_Trabalho3
   ```

2. Instale as dependências (via `rosdep`):
   ```bash
   rosdep install --from-paths src --ignore-src -r -y
   ```

3. Compile o workspace:
   ```bash
   colcon build
   ```

4. Fonte o ambiente:
   ```bash
   source install/setup.bash
   ```

5. Execute o mundo no Gazebo e os nós ROS 2:
   ```bash
   ros2 launch <pacote> <arquivo_launch>.launch.py
   ```

6. Abra o RViz:
   ```bash
   ros2 run rviz2 rviz2 -d rviz/<arquivo_config>.rviz
   ```

---

## 🧭 Funcionalidades

- Modelagem probabilística de sensores e movimentos  
- Localização e mapeamento com incertezas  
- Visualização em tempo real com Gazebo e RViz  
- Scripts para testes automatizados e avaliação de desempenho

---

## 📚 Referências

Este trabalho baseia‑se em:

- Documentação ROS 2  
- Tutoriais do Gazebo  
- Artigos clássicos de Robótica Probabilística (filtros de Kalman, MCL, etc.)

---

## 📝 Licença

Este projeto está disponível sob a licença [MIT](LICENSE). Fique à vontade para usar, modificar e distribuir.

---

## 📞 Contato

Em caso de dúvidas, sugestões ou contribuições:

- **Michael Lima** – michael@example.com  
- **Arthur Fellini** – arthur@example.com  
- **Pedro Henrique Themoteo** – pedro@example.com  

---

## ⭐ Agradecimentos

Agradecemos ao professor e colegas da disciplina pela orientação e feedback construtivo. Bom estudo! 🚀
