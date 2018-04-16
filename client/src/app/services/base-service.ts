export class BaseService {
    baseAddress: string;

    constructor(address) {
        this.baseAddress = `/api/${address}`;
    }
}