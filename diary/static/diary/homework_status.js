const buttons = document.querySelectorAll(`.done_btn`)

for (let btn of buttons){
    btn.addEventListener(`click`, async ()=>{
        console.log(btn.id)
        const url = "/homework/update/";
        try {
            const response = await fetch(url, {
                method: "POST",
                body: JSON.stringify({ 'id': `${btn.id}`, 'status': 'd' }),
            });
            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }

            const item = document.querySelector(`#li_${btn.id}`) 
            item.remove()
            }
      catch (error) {
            console.error(error.message);
      }

    })
}
