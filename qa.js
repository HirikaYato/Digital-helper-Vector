const Orders = [
    {
        Request: 'How are u?',
        Request_keyword: "how, a, u",
        Answer: 'good',
        FileName: 'test',
        FileHref: 'https://images.unsplash.com/photo-1554080353-a576cf803bda?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cGhvdG98ZW58MHx8MHx8fDA%3D'
    },
    {
        Request: 'How are u?',
        Request_keyword: "how, a, u",
        Answer: 'good',
        File: '',
        FileHref: ''
    },
    {
        Request: 'How are u?',
        Request_keyword: "how, a, u",
        Answer: 'good',
        File: '',
        FileHref: ''
    },
    {
        Request: 'How are u?',
        Request_keyword: "how, a, u",
        Answer: 'good',
        File: '',
        FileHref: ''
    },
]

Orders.forEach(order => {
    const tr = document.createElement('tr');
    const trContent = `
        <td>${order.Request}</td>
        <td>${order.Request_keyword}</td>
        <td>${order.Answer}</td>
        <td> <a href="${order.FileHref}" target="_blank">
            <button class="custom-btn btn-16">${order.FileName}</button>
        </a></td>
        <td><button class="custom-btn btn-16">Удалить</button></td>`

    tr.innerHTML = trContent;
    document.querySelector('table tbody').appendChild(tr);
})