# Proposição do Teste:

Neste desafio, será realizada a simulação controlada de dois tipos clássicos de malware em um ambiente seguro e exclusivamente educacional: Ransomware e Keylogger.

A proposta consiste em compreender, na prática, como essas ameaças funcionam, como exploram vulnerabilidades técnicas e comportamentais, e principalmente como podemos detectá-las, mitigá-las e preveni-las em ambientes corporativos e pessoais.

A jornada técnica começa com a criação de arquivos de teste e a implementação de um Ransomware Simulado utilizando Python e criptografia com a biblioteca Cryptography (Fernet), permitindo observar o processo de sequestro e recuperação de dados.

Em seguida, será realizada a simulação de um Keylogger controlado, registrando entradas de teclado em arquivo local para fins acadêmicos, demonstrando como ocorre a captura de informações sensíveis e reforçando a importância de mecanismos de defesa e conscientização do usuário.

Além da implementação prática, o desafio também propõe uma reflexão crítica sobre segurança da informação, abordando estratégias de defesa como antivírus, firewall, EDR, sandboxing, backup, MFA e boas práticas de segurança operacional.

O objetivo principal não é a criação de malware funcional, mas sim o entendimento técnico necessário para reconhecer ameaças reais e fortalecer a postura defensiva em cibersegurança.

---

# Palavras-chave:

- Python;
- Ransomware;
- Keylogger;
- Cryptography;
- Fernet;
- Segurança da Informação;
- Malware;
- Defesa Cibernética;
- Backup;
- MFA;
- EDR;

---

# Explicações

A proposta do desafio foi desenvolver um ambiente de simulação de malware com foco educacional e defensivo.

Para atingir esse objetivo, foi utilizada a linguagem Python juntamente com a biblioteca Cryptography (Fernet) para simular o comportamento de um Ransomware, realizando a criptografia e posterior descriptografia de arquivos de teste.

Também foi realizada a simulação de um Keylogger controlado, registrando entradas de teclado em arquivo local para fins de estudo, sem mecanismos de persistência, ocultação ou envio externo, mantendo o ambiente totalmente seguro e responsável.

Além da parte prática, foram documentadas as principais medidas de prevenção e defesa contra esse tipo de ameaça, reforçando a importância da segurança em camadas e da conscientização dos usuários.

---

# Organização do projeto

A estrutura do projeto está conforme alinhado abaixo:

|- README.md  
|  
|- ransomware_simulation/  
|   |- encrypt.py -> (script de criptografia dos arquivos de teste)  
|   |- decrypt.py -> (script de descriptografia dos arquivos)  
|   |- ransom_note.txt -> (mensagem de simulação de resgate)  
|   |  
|   |- test_files/  
|       |- exemplo.txt -> (arquivo utilizado para testes)  
|  
|- keylogger_simulation/  
|   |- simulated_logger.py -> (simulação controlada de captura de teclado)  
|   |  
|   |- logs/  
|       |- keystrokes.txt -> (arquivo com os registros simulados)  
|  
|- defense_notes.md -> (documentação sobre prevenção e defesa)  
|  
|- requirements.txt -> (bibliotecas utilizadas no projeto)  
|  
|- images/  
|   |- screenshots.png -> (capturas de tela opcionais)

---

# Aviso Importante

Este projeto possui finalidade exclusivamente educacional e foi desenvolvido em ambiente controlado para fins de aprendizado em cibersegurança.

Nenhum dos códigos aqui presentes deve ser utilizado fora de laboratórios autorizados, ambientes de teste ou contextos acadêmicos.

O foco principal deste repositório é a compreensão técnica de ameaças reais e o fortalecimento de estratégias de defesa e prevenção.