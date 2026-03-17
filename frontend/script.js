document.addEventListener('DOMContentLoaded', () => {
    const sectorInput = document.getElementById('sectorInput');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const loader = document.getElementById('loader');
    const reportContainer = document.getElementById('reportContainer');
    const reportContent = document.getElementById('reportContent');
    const reportTitle = document.getElementById('reportTitle');
    const downloadBtn = document.getElementById('downloadBtn');

    let currentMarkdown = "";
    let currentSector = "";

    const handleAnalyze = async () => {
        const sector = sectorInput.value.trim();
        if (!sector) {
            alert("Please enter a sector name");
            return;
        }

        currentSector = sector;
        
        // UI State: Loading
        analyzeBtn.disabled = true;
        loader.classList.remove('hidden');
        reportContainer.classList.add('hidden');

        try {
            const response = await fetch(`/api/v1/analyze/${encodeURIComponent(sector)}`);
            const data = await response.json();

            if (response.ok) {
                currentMarkdown = data.report_markdown;
                reportContent.innerHTML = marked.parse(currentMarkdown);
                reportTitle.innerText = `Market Analysis: ${sector.charAt(0).toUpperCase() + sector.slice(1)}`;
                reportContainer.classList.remove('hidden');
            } else {
                alert(`Error: ${data.detail || "Failed to analyze sector"}`);
            }
        } catch (error) {
            console.error("API Error:", error);
            alert("Connection error. Is the backend running?");
        } finally {
            analyzeBtn.disabled = false;
            loader.classList.add('hidden');
        }
    };

    analyzeBtn.addEventListener('click', handleAnalyze);
    sectorInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleAnalyze();
    });

    downloadBtn.addEventListener('click', () => {
        if (!currentMarkdown) return;
        
        const blob = new Blob([currentMarkdown], { type: 'text/markdown' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${currentSector}_analysis.md`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    });
});
