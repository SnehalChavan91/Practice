function calculateAge() {
    const birthdateInput = document.getElementById("birthdate").value;
    const resultDiv = document.getElementById('result');

    if (!birthdateInput) {
        document.getElementById('result').textContent = 'Please select your birthdate.';
        return;
    }

    const birthdate = new Date(birthdateInput);
    const today = new Date();

    let ageYears = today.getFullYear() - birthdate.getFullYear();
    let ageMonths = today.getMonth() - birthdate.getMonth();
    let ageDays = today.getDate() - birthdate.getDate();

    if (ageDays < 0) {
        ageMonths--;
        ageDays += new Date(today.getFullYear(), today.getMonth(), 0).getDate();
    }

    if (ageMonths < 0) {
        ageYears--;
        ageMonths += 12;
    }

    document.getElementById('result').textContent =  `You are ${ageYears} years, ${ageMonths} months , and ${ageDays} days old.`;
    // document.getElementById('textResult').textContent = `You are ${ageYears} years, ${ageMonths} months , and ${ageDays} days old.`
}